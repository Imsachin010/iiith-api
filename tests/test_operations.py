def get_token(client, username="admin", password="admin"):
    response = client.post("/token", data={"username": username, "password": password})
    return response.json()["access_token"]

def test_add(client):
    token = get_token(client)
    response = client.post("/add", json={"a": 5, "b": 3}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["result"] == 8

def test_multiply(client):
    token = get_token(client)
    response = client.post("/multiply", json={"a": 4, "b": 6}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["result"] == 24

def test_even_odd(client):
    token = get_token(client)
    response = client.get("/evenodd/7", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["result"] == "odd"
