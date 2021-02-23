import pytest


@pytest.mark.gen_test(timeout=15)
def test_avatar(http_client, base_url):
    response = yield http_client.fetch(base_url + '/avatar/avatar_test')
    assert response.code == 200