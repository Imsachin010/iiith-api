def get_token(client, username="admin", password="admin"):
    response = client.post("/token", data={"username": username, "password": password})
    return response.json()["access_token"]

def test_logs_admin_access(client):
    token = get_token(client)
    response = client.get("/logs?limit=2&offset=0", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_logs_non_admin_forbidden(client):
    token = get_token(client, username="user", password="user")
    response = client.get("/logs", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403
