def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Ожидали {expected_code}, получили {response.status_code}"


def assert_response_json(response):
    try:
        return response.json()
    except ValueError:
        assert False, "Ответ не в JSON формате"