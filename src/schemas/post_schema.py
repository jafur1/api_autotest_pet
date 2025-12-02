POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "userId": {"type": "integer", "minimum": 1},
        "title": {"type": "string", "minLength": 1},
        "body": {"type": "string", "minLength": 1}
    },
    "required": ["id", "userId", "title", "body"],
    "additionalProperties": False
}

POST_COMMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "postId": {"type": "integer", "minimum": 1},
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1},
        "email": {"type": "string", "minLength": 1},
        "body": {"type": "string", "minLength": 1}
    },
    "required": ["postId", "id", "name", "email", "body"],
    "additionalProperties": False
}
