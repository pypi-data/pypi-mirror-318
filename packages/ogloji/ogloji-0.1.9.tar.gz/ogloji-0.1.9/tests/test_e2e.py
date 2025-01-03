import datetime
import io
import os
import time
import uuid
from threading import Thread

import imagehash
import pytest
import requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.testclient import TestClient
from PIL import Image

from ogloji import app

OG_IMAGE_FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "og-image-fixture.png")
INLINE_FONT_STYLE_PATH = os.path.join(
    os.path.dirname(__file__), "inline-font-style.html"
)

# This is the app we're going to take screenshots of OG images from.
html_app = FastAPI()


@html_app.get("/up")
async def up():
    return {"status": "up"}


@html_app.get("/random")
async def serve_random_page():
    with open(INLINE_FONT_STYLE_PATH, "r") as f:
        inline_font_style = f.read()
    random_uuid = uuid.uuid4()
    return Response(
        content=f"""
    <!DOCTYPE html>
    <html>
        <head>
            {inline_font_style}
        </head>
        <body style="margin: 0;">
            <div id="og-image" style="width: 1200px; height: 630px; background: #f0f0f0; display: flex; justify-content: center; align-items: center;">
                <span style="font-size: 48px;">Test OG Image {random_uuid}</span>
            </div>
        </body>
    </html>
    """,
        media_type="text/html",
    )


@html_app.get("/{path:path}")
async def serve_test_page():
    with open(INLINE_FONT_STYLE_PATH, "r") as f:
        inline_font_style = f.read()
    return Response(
        content=f"""
    <!DOCTYPE html>
    <html>
        <head>
            {inline_font_style}
        </head>
        <body style="margin: 0;">
            <div id="og-image" style="width: 1200px; height: 630px; background: #f0f0f0; display: flex; justify-content: center; align-items: center;">
                <span style="font-size: 48px;">Test OG Image</span>
            </div>
        </body>
    </html>
    """,
        media_type="text/html",
    )


def run_test_server():
    uvicorn.run(html_app, host="127.0.0.1", port=9001, log_level="error")


@pytest.fixture(autouse=True, scope="session")
def setup_html_server():
    client = TestClient(html_app)

    # Start the test HTML server
    server_thread = Thread(target=run_test_server, daemon=True)
    server_thread.start()

    # Wait for server to be ready by polling the /up endpoint
    timeout_seconds = 5
    start_time = time.time()

    while time.time() - start_time < timeout_seconds:
        try:
            response = client.get("/up")
            if response.status_code == 200:
                break
        except (ConnectionRefusedError, requests.exceptions.ConnectionError):
            time.sleep(0.1)
    else:
        raise RuntimeError(
            f"Test server failed to start within {timeout_seconds} seconds"
        )

    yield


def image_equal(image1: bytes, image2: bytes):
    img1 = Image.open(io.BytesIO(image1))
    img2 = Image.open(io.BytesIO(image2))

    hash1 = imagehash.phash(img1)
    hash2 = imagehash.phash(img2)

    return hash1 == hash2


def save_test_images(actual_content, expected_content, test_name):
    # Create test-output directory if it doesn't exist
    os.makedirs("test-output", exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save both images with descriptive names
    actual_path = f"test-output/{test_name}_actual_{timestamp}.png"
    expected_path = f"test-output/{test_name}_expected_{timestamp}.png"

    with open(actual_path, "wb") as f:
        f.write(actual_content)
    with open(expected_path, "wb") as f:
        f.write(expected_content)

    return actual_path, expected_path


def test_e2e(monkeypatch, tmp_path):
    monkeypatch.setenv("BROWSER_POOL_SIZE", "2")
    monkeypatch.setenv("BASE_URL", "http://localhost:9001")
    monkeypatch.setenv("LOCAL_STORAGE_PATH", str(tmp_path / "images"))
    monkeypatch.setenv("API_KEY", "test_api_key")
    with TestClient(app) as client:
        try:
            # Test the happy path -- an image we know is generated.
            response = client.get("/og-image/test")
            assert response.status_code == 200
            assert response.headers["content-type"] == "image/png"
            with open(OG_IMAGE_FIXTURE_PATH, "rb") as f:
                expected_image = f.read()
            assert image_equal(response.content, expected_image)
        except AssertionError as e:
            save_test_images(response.content, expected_image, "happy_path")
            raise e

        try:
            # The first time we request a random page, it should be generated.
            response = client.get("/og-image/random")
            assert response.status_code == 200
            assert response.headers["content-type"] == "image/png"
            first_random_image = response.content
        except AssertionError as e:
            save_test_images(response.content, None, "first_random_page")
            raise e

        try:
            # The second time we request a random page from the same path, it'll
            # be served from cache, so we should get the same image.
            response = client.get("/og-image/random")
            assert response.status_code == 200
            assert response.headers["content-type"] == "image/png"
            assert image_equal(response.content, first_random_image)
        except AssertionError as e:
            save_test_images(response.content, first_random_image, "second_random_page")
            raise e

        try:
            # Purging and re-requesting the random page should generate a new image.
            response = client.post(
                "/purge-og-image",
                json={"request_uris": ["/random"]},
                headers={"X-API-Key": "test_api_key"},
            )
            assert response.status_code == 200
            response = client.get("/og-image/random")
            assert response.status_code == 200
            assert response.headers["content-type"] == "image/png"
            assert not image_equal(response.content, first_random_image)
        except AssertionError as e:
            save_test_images(
                response.content, first_random_image, "purge_then_request_random_page"
            )
            raise e

        try:
            # When we add query params, it should be treated as a new image.
            response = client.get("/og-image/random?a=1&b=2")
            assert response.status_code == 200
            assert response.headers["content-type"] == "image/png"
            assert not image_equal(response.content, first_random_image)
            first_query_params_image = response.content
        except AssertionError as e:
            save_test_images(response.content, first_random_image, "query_params_order")
            raise e

        try:
            # The order of query params should not matter. We should get the
            # same image served from cache.
            response = client.get("/og-image/random?b=2&a=1")
            assert response.status_code == 200
            assert response.headers["content-type"] == "image/png"
            assert image_equal(response.content, first_query_params_image)
        except AssertionError as e:
            save_test_images(
                response.content, first_query_params_image, "query_params_unordered"
            )
            raise e

        try:
            # When purging, the order of query params should not matter.
            response = client.post(
                "/purge-og-image",
                json={"request_uris": ["/random?b=2&a=1"]},
                headers={"X-API-Key": "test_api_key"},
            )
            assert response.status_code == 200
            response = client.get("/og-image/random?a=1&b=2")
            assert response.status_code == 200
            assert response.headers["content-type"] == "image/png"
            assert not image_equal(response.content, first_query_params_image)
        except AssertionError as e:
            save_test_images(
                response.content,
                first_query_params_image,
                "purge_then_request_query_params_unordered",
            )
            raise e


def test_api_key_not_set_always_unauthorized(monkeypatch, tmp_path):
    monkeypatch.setenv("BROWSER_POOL_SIZE", "1")
    monkeypatch.setenv("BASE_URL", "http://localhost:9001")
    monkeypatch.setenv("LOCAL_STORAGE_PATH", str(tmp_path / "images"))
    monkeypatch.delenv("API_KEY", raising=False)
    with TestClient(app) as client:
        response = client.post(
            "/purge-og-image",
            json={"request_uris": ["/test"]},
            headers={"X-API-Key": ""},
        )
        assert response.status_code == 401
        response = client.post(
            "/purge-og-image",
            json={"request_uris": ["/test"]},
            headers={"X-API-Key": "None"},
        )
        assert response.status_code == 401
        response = client.post(
            "/purge-og-image",
            json={"request_uris": ["/test"]},
            headers={"X-API-Key": "test_api_key"},
        )
        assert response.status_code == 401
        response = client.post(
            "/purge-og-image",
            json={"request_uris": ["/test"]},
        )
        assert response.status_code == 401


def test_api_key_when_set_is_authorized(monkeypatch, tmp_path):
    monkeypatch.setenv("BROWSER_POOL_SIZE", "1")
    monkeypatch.setenv("BASE_URL", "http://localhost:9001")
    monkeypatch.setenv("LOCAL_STORAGE_PATH", str(tmp_path / "images"))
    monkeypatch.setenv("API_KEY", "my_test_api_key")
    with TestClient(app) as client:
        response = client.post(
            "/purge-og-image",
            json={"request_uris": ["/test"]},
            headers={"X-API-Key": "my_test_api_key"},
        )
        assert response.status_code == 200
        response = client.post(
            "/purge-og-image",
            json={"request_uris": ["/test"]},
            headers={"X-API-Key": "wrong_api_key"},
        )
        assert response.status_code == 401
