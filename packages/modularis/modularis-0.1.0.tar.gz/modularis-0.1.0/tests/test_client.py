import pytest
from modularis import Client, Response
from modularis.middleware import Middleware
from modularis.interceptor import Interceptor
from typing import Dict, Any
import aiohttp
import json

# Fixtures
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def client(base_url):
    return Client(base_url=base_url)

# Test Middleware
class TestMiddleware(Middleware):
    def __init__(self):
        self.called = False
    
    def before_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        self.called = True
        return request

# Test Interceptor
class TestInterceptor(Interceptor):
    def __init__(self):
        self.called = False
    
    def before_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        self.called = True
        if "headers" not in request:
            request["headers"] = {}
        request["headers"]["X-Test"] = "test"
        return request

# Tests
@pytest.mark.asyncio
async def test_client_creation(client):
    assert client.base_url == "https://jsonplaceholder.typicode.com"
    assert isinstance(client.session, aiohttp.ClientSession)

@pytest.mark.asyncio
async def test_get_request(client):
    response = await client.get("/posts/1")
    assert response.status_code == 200
    assert response.data["id"] == 1
    assert "title" in response.data

@pytest.mark.asyncio
async def test_post_request(client):
    data = {
        "title": "Test Post",
        "body": "This is a test post",
        "userId": 1
    }
    response = await client.post("/posts", json=data)
    assert response.status_code == 201
    assert response.data["title"] == "Test Post"

@pytest.mark.asyncio
async def test_middleware(client):
    middleware = TestMiddleware()
    client.add_middleware(middleware)
    
    response = await client.get("/posts/1")
    assert middleware.called
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_interceptor(client):
    interceptor = TestInterceptor()
    client.add_interceptor(interceptor)
    
    response = await client.get("/posts/1")
    assert interceptor.called
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_error_handling(client):
    with pytest.raises(Exception):
        await client.get("/nonexistent")

@pytest.mark.asyncio
async def test_response_json(client):
    response = await client.get("/posts/1")
    assert isinstance(response.data, dict)
    assert response.headers is not None
    assert isinstance(response.elapsed, float)

@pytest.mark.asyncio
async def test_query_params(client):
    response = await client.get("/posts", params={"userId": 1})
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert all(post["userId"] == 1 for post in response.data)

@pytest.mark.asyncio
async def test_custom_headers(client):
    headers = {"X-Custom-Header": "test"}
    response = await client.get("/posts/1", headers=headers)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_timeout(client):
    client.timeout = 5
    response = await client.get("/posts/1")
    assert response.status_code == 200

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
