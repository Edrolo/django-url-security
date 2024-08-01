# ruff: noqa: PLR2004  # Allow magic numbers like 200

from fastapi.testclient import TestClient

from django_url_security.fastapi import UrlSecurityTestCase

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}


class MyTestCase(UrlSecurityTestCase):
    app = app
