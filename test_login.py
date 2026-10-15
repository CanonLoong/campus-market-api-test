import requests

base_url = 'http://localhost:8080'
def test_login():
    url = base_url + '/api/auth/login'
    data = {'username': 'admin', 'password': 'admin123'}
    res = requests.post(url, json=data)
    assert res.status_code == 200
    assert res.json()['code'] ==200

def test_login_wrong_password():
    url = base_url + '/api/auth/login'
    data = {'username': 'admin', 'password': 'amin123'}
    res = requests.post(url, json=data)
    assert res.json()['code'] != 200
