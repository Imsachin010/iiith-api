from locust import HttpUser, task, between, events
import json
from datetime import datetime

class APIUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks

    def on_start(self):
        """Initialize user session with authentication"""
        try:
            # Login and get token
            response = self.client.post(
                "/token",
                data={"username": "admin", "password": "adminpass"}
            )
            if response.status_code == 200:
                self.token = response.json()["access_token"]
                self.headers = {"Authorization": f"Bearer {self.token}"}
            else:
                print(f"Failed to authenticate: {response.text}")
        except Exception as e:
            print(f"Error during authentication: {str(e)}")

    @task(3)  # Higher weight for add operation
    def add_numbers(self):
        """Test addition endpoint"""
        payload = {"num1": 10, "num2": 20}
        with self.client.post(
            "/add",
            json=payload,
            headers=self.headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                result = response.json()
                if result.get("result") == 30:
                    response.success()
                else:
                    response.failure("Incorrect addition result")
            else:
                response.failure(f"Failed with status {response.status_code}")

    @task(2)  # Medium weight for multiply operation
    def multiply_numbers(self):
        """Test multiplication endpoint"""
        payload = {"num1": 4, "num2": 5}
        with self.client.post(
            "/multiply",
            json=payload,
            headers=self.headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                result = response.json()
                if result.get("result") == 20:
                    response.success()
                else:
                    response.failure("Incorrect multiplication result")
            else:
                response.failure(f"Failed with status {response.status_code}")

    @task(1)  # Lower weight for even/odd check
    def check_even_odd(self):
        """Test even/odd check endpoint"""
        with self.client.get(
            "/check-even-odd?number=7",
            headers=self.headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                result = response.json()
                if result.get("result") == "odd":
                    response.success()
                else:
                    response.failure("Incorrect even/odd result")
            else:
                response.failure(f"Failed with status {response.status_code}")

@events.test_start.add_listener
def on_test_start(**kwargs):
    """Log test start time"""
    print(f"Performance test started at: {datetime.now()}")

@events.test_stop.add_listener
def on_test_stop(**kwargs):
    """Log test end time"""
    print(f"Performance test ended at: {datetime.now()}")
