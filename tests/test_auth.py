def test_login_success(client):
    response = client.post("/token", data={"username": "admin", "password": "admin"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_failure(client):
    response = client.post("/token", data={"username": "wrong", "password": "bad"})
    assert response.status_code == 401
