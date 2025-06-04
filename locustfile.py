from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        # Login once and store token
        res = self.client.post("/token", data={"username": "admin", "password": "admin"})
        self.token = res.json()["access_token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    @task
    def add_numbers(self):
        self.client.post("/add", json={"a": 10, "b": 20}, headers=self.headers)

    @task
    def multiply_numbers(self):
        self.client.post("/multiply", json={"a": 4, "b": 5}, headers=self.headers)

    @task
    def even_or_odd(self):
        self.client.get("/evenodd/7", headers=self.headers)
