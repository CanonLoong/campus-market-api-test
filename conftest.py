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

@pytest.fixture(scope='session')
def buyer_token():
    url = base_url + '/api/auth/login'
    data = {'username': 'buyer01', 'password': 'buyer123'}
    res = requests.post(url, json=data)
    assert res.status_code == 200
    token = res.json()['data']['token']
    return token

@pytest.fixture(scope='session')
def seller_token():
    url = base_url + '/api/auth/login'
    data = {'username': 'seller01', 'password': 'seller123'}  # 换成你的卖家账号
    res = requests.post(url, json=data)
    assert res.json()['code'] == 200
    return res.json()['data']['token']