import pytest
import requests

base_url = 'http://localhost:8080'
@pytest.fixture(scope='session')
def token():
    url = base_url + '/api/auth/login'
    data = {'username': 'admin', 'password': 'admin123'}
    res = requests.post(url, json=data)
    assert res.status_code == 200
    token = res.json()['data']['token']
    return token