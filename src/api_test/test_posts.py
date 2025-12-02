import pytest
import helpers
import jsonschema
from src.schemas.post_schema import POST_SCHEMA, POST_COMMENT_SCHEMA


class TestPosts:
    def test_get_all_posts(self, api_client):
        respons = api_client.get("/posts")
        helpers.assert_status_code(respons, 200)
        posts = helpers.assert_response_json(respons)
        assert len(posts) == 100, f"Ожидалось 100 постов, было получено {len(posts)}"

    def test_get_one_post(self, api_client):
        respons = api_client.get("/posts/1")
        helpers.assert_status_code(respons, 200)
        post = helpers.assert_response_json(respons)
        jsonschema.validate(instance=post, schema=POST_SCHEMA)
        assert post['id'] == 1

    def test_create_post(self, api_client, test_post_data):
        respons = api_client.post("/posts", test_post_data)
        helpers.assert_status_code(respons, 201)
        post = helpers.assert_response_json(respons)
        jsonschema.validate(instance=post, schema=POST_SCHEMA)
        assert post['title'] == test_post_data['title']
        assert post['body'] == test_post_data['body']
        assert post['userId'] == test_post_data['userId']

    def test_update_post(self, api_client):
        update_data = {
            "title": "updated title",
            "body": "updated body",
            "userId": 2
        }
        old_response = api_client.get("/posts/1")
        helpers.assert_status_code(old_response, 200)
        old_post = helpers.assert_response_json(old_response)
        assert old_post['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'
        assert old_post['body'] == 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'

        respons = api_client.put("/posts/1", update_data)
        helpers.assert_status_code(respons, 200)
        post = helpers.assert_response_json(respons)
        assert post['title'] == 'updated title'
        assert post['body'] == 'updated body'

    def test_delete_post(self, api_client):
        respons = api_client.delete("/posts/1")
        helpers.assert_status_code(respons, 200)
        post = helpers.assert_response_json(respons)
        assert post == {}

    def test_post_comment(self, api_client):
        respons = api_client.get("/posts/1/comments")
        helpers.assert_status_code(respons, 200)
        comments = helpers.assert_response_json(respons)
        jsonschema.validate(instance=comments[0], schema=POST_COMMENT_SCHEMA)

    def test_create_comment(self, api_client, test_post_data):
        test_post_data = {
            "name": "Test Commenter",
            "email": "commenter@example.com",
            "body": "This is a test comment."
        }
        respons = api_client.post("/posts/1/comments", test_post_data)
        helpers.assert_status_code(respons, 201)
        comment = helpers.assert_response_json(respons)
        assert comment['name'] == 'Test Commenter'
        assert comment['body'] == 'This is a test comment.'












