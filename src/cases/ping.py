import pytest

@pytest.mark.gen_test(timeout=15)
def test_ping(http_client, base_url):
    response = yield http_client.fetch(base_url + '/ping')
    assert response.code == 200