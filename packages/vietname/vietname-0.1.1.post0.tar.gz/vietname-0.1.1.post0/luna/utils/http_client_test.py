from .http_client import SimpleHttpClient


def test_absolute_url():
    client = SimpleHttpClient()
    res = client.get("https://google.com")
    assert res.status_code == 200


def test_relative_url():
    client = SimpleHttpClient(base_url="https://github.com")
    res = client.get("/square/certstrap")
    assert res.status_code == 200
