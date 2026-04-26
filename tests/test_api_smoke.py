"""Smoke tests for Santa Fe CI API.
Run after install with: pytest project/tests/test_api_smoke.py
"""
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_core_endpoints():
    for path in [
        '/api/health',
        '/api/system/health',
        '/api/feed',
        '/api/alerts',
        '/api/listings',
        '/api/openapi.json',
    ]:
        response = client.get(path)
        assert response.status_code == 200, path


def test_feed_shape():
    data = client.get('/api/feed').json()
    assert 'buildings' in data
    assert 'tower_summary' in data
    assert 'market_summary' in data
    assert 'listings' in data
    assert 'alerts' in data
    assert 'health' in data
    assert isinstance(data['listings'], list)


def test_system_health_shape():
    data = client.get('/api/system/health').json()
    for key in ['api', 'data', 'database', 'feed', 'alerts', 'scoring', 'sources', 'cache', 'readiness']:
        assert key in data
