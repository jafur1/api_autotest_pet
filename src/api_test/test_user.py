import requests
import pytest
import jsonschema
from src.schemas.user_schema import USER_SCHEMA
import helpers

class TestUser:
    def test_get_user(self, api_client):
        response = api_client.get('/users')
        helpers.assert_status_code(response, 200)
        users = helpers.assert_response_json(response)
        assert isinstance(users, list), "Ответ должен быть списком"
        first_user = users[0]
        jsonschema.validate(instance=first_user, schema=USER_SCHEMA)

    def test_get_first_user(self, api_client):
        response = api_client.get('/users/1')
        helpers.assert_status_code(response, 200)
        users = helpers.assert_response_json(response)
        assert users['id'] == 1
        assert users["name"] == "Leanne Graham"
        assert users["email"] == "Sincere@april.biz"
        assert '@' in users["email"]

    def test_creat_user(self,api_client,user_data):
        response = api_client.post('/users', user_data)
        helpers.assert_status_code(response, 201)
        creat_user = helpers.assert_response_json(response)
        assert creat_user['name'] == user_data["name"]
        assert creat_user['email'] == user_data["email"]
        assert creat_user['username'] == user_data["username"]
        assert 'id' in creat_user

    def test_update_put_user(self, api_client):
        update_data = {
            "name": "Updated Name",
            "email": "updated@example.com"
        }
        response = api_client.put('/users/1', update_data)
        helpers.assert_status_code(response, 200)
        response_data = helpers.assert_response_json(response)
        assert response_data["name"] == "Updated Name"
        assert response_data["email"] == "updated@example.com"

    def test_update_patch_user(self, api_client):
        update_data = {
            "name": "Patched Name",
            "email": "patched@example.com"
        }
        response = api_client.patch('/users/1', update_data)
        helpers.assert_status_code(response, 200)
        response_data = helpers.assert_response_json(response)
        assert response_data["name"] == "Patched Name"
        assert response_data["email"] == "patched@example.com"

    def test_delete_user(self, api_client):
        response = api_client.delete('/users/1')
        helpers.assert_status_code(response, 200)
        response_data = helpers.assert_response_json(response)
        assert response_data == {} or len(response_data) == 0

    def test_nonexistent_user(self, api_client):
        response = api_client.get('/users/9129321393219321')
        helpers.assert_status_code(response, 404)

    def test_create_minimal_data_user(self, api_client):
        user_data = {'name': 'damir'}
        response = api_client.post('/users', user_data)
        helpers.assert_status_code(response, 201)
        users = helpers.assert_response_json(response)
        assert users['name'] == 'damir'

    def test_user_with_zero_id(self, api_client):
        response = api_client.get('/users/0')
        helpers.assert_status_code(response, 404)
        users = helpers.assert_response_json(response)
        assert users == {}



    @pytest.mark.parametrize("user_id, expected_name",[(1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")])
    def test_multiple_users(self, api_client,user_id, expected_name):
        response = api_client.get(f'/users/{user_id}')
        helpers.assert_status_code(response, 200)
        user = helpers.assert_response_json(response)
        assert user["name"] == expected_name, f"Проверяли {user_id}: {expected_name}"


