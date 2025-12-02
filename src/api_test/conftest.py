import pytest
from src.api_client.api_client_main import ApiClient

@pytest.fixture
def api_client():
    return ApiClient()

@pytest.fixture
def user_data():
    return {
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com",
        "address": {
            "street": "Test Street",
            "suite": "Apt. 1",
            "city": "Test City",
            "zipcode": "12345",
            "geo": {"lat": "0.0", "lng": "0.0"}
        },
        "phone": "1-234-567-8900",
        "website": "https://test.example.com",
        "company": {
            "name": "Test Company",
            "catchPhrase": "Test catch phrase",
            "bs": "Test business"
        }
    }

@pytest.fixture
def invalid_data():
    return {
        "username": " ",
            "email": "not_email"}

@pytest.fixture
def test_post_data():
    return {
        "title": "Test Post Title",
        "body": "This is a test post body content.",
        "userId": 1
    }