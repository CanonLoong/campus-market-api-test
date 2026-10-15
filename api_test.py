import requests

base_url = 'http://localhost:8080'
def get_token():
    url = base_url + '/api/auth/login'
    data = {'username': 'admin', 'password': 'admin123'}
    response = requests.post(url, json=data)
    print(response.json())
    print(response.status_code)

    assert response.status_code == 200

    token = response.json()['data']['token']

    print(token)
    return token
if __name__ == '__main__':
    get_token()