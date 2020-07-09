from main import get_temperature
import requests
import pytest


class MockResponse:
    @staticmethod
    def json():
        return {'latitude': -14.235004,
                'longitude': -51.92528,
                'currently': {'temperature': 62}}


@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


def test_get_temperature_by_lat_lng(mock_response):
    assert get_temperature(-14.235004, -51.92528) == 16
