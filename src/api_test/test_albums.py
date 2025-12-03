import pytest
import helpers
import jsonschema
from src.schemas.albums_schema import ALBUMS_SCHEMA

class TestAlbums:
    def test_get_albums(self,api_client):
        response = api_client.get('/albums')
        helpers.assert_status_code(response, 200)
        albums = helpers.assert_response_json(response)
        assert len(albums) == 100

    def test_get_specific_albums(self,api_client):
        response = api_client.get('/albums/1')
        helpers.assert_status_code(response, 200)
        album = helpers.assert_response_json(response)
        assert album['userId'] == 1
        assert album['id'] == 1
        assert "title" in album

    def test_create_album(self,api_client):
        test_data = {
            'userId': 1,
            'title': 'test create album',
        }
        response = api_client.post('/albums', test_data)
        helpers.assert_status_code(response, 201)
        album = helpers.assert_response_json(response)
        assert 'id' in album
        assert album['userId'] == 1
        assert album['title'] == 'test create album'

    def test_update_album(self,api_client):
        test_data = {
            'userId': 2,
            'title': 'test update album'
        }
        response = api_client.put('/albums/1', test_data)
        helpers.assert_status_code(response, 200)
        album = helpers.assert_response_json(response)
        assert 'id' in album
        assert album['userId'] == 2
        assert album['title'] == 'test update album'

    def test_delete_album(self,api_client):
        response = api_client.delete('/albums/1')
        helpers.assert_status_code(response, 200)

    def test_validate_schema_albums(self,api_client):
        response = api_client.get('/albums/1')
        helpers.assert_status_code(response, 200)
        album = helpers.assert_response_json(response)
        jsonschema.validate(album, ALBUMS_SCHEMA)
