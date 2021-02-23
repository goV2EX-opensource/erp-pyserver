import mimetypes
from functools import partial
from uuid import uuid4

import pytest
from tornado import gen


@gen.coroutine
def raw_producer(filename, write):
    with open(filename, "rb") as f:
        while True:
            # 16K at a time.
            chunk = f.read(16 * 1024)
            if not chunk:
                # Complete.
                break

            yield write(chunk)


@pytest.mark.gen_test(timeout=15)
def test_avatar(http_client, base_url):
    response = yield http_client.fetch(base_url + '/avatar/avatar_test')
    assert response.code == 200


@pytest.mark.gen_test(timeout=15)
def test_upload_avatar_jpeg(http_client, base_url):
    boundary = uuid4().hex
    filename = './test_resources/test.jpg'
    mtype = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    headers = {"Content-Type": mtype}
    producer = partial(raw_producer, filename)
    response = yield http_client.fetch(
        base_url + r'/avatar',
        method="POST",
        headers=headers,
        body_producer=producer,
    )
    assert response.code == 200
