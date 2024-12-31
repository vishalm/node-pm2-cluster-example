from locust import HttpUser, TaskSet, task, between

# Define tasks for the first app
class NodeAppObservabilityTasks(TaskSet):
    @task(1)
    def health_check(self):
        response = self.client.get("/health-check")
        assert response.status_code == 200, f"Health check failed with {response.status_code}"

    @task(2)
    def about(self):
        response = self.client.get("/about")  # Replace with your endpoint
        assert response.status_code == 200, f"About failed with with {response.status_code}"

    @task(3)
    def home(self):
        response = self.client.get("/")  # Replace with actual payload
        assert response.status_code == 200, f"Home failed with {response.status_code}"

    @task(4)
    def custom(self):
        response = self.client.get("/custom")  # Replace with actual payload
        assert response.status_code == 200, f"Custom failed with {response.status_code}"

    @task(6)
    def actuator_info(self):
        response = self.client.get("/actuator/info")
        assert response.status_code == 200, f"/actuator/info failed with {response.status_code}"

    @task(6)
    def actuator_info(self):
        response = self.client.get("/actuator/info")
        assert response.status_code == 200, f"/actuator/info failed with {response.status_code}"

    @task(7)
    def actuator_health(self):
        response = self.client.get("/actuator/health")
        assert response.status_code == 200, f"/actuator/health failed with {response.status_code}"

    @task(8)
    def metrics(self):
        response = self.client.get("/metrics")
        assert response.status_code == 200, f"/metrics failed with {response.status_code}"



# Define tasks for the second app
class NodeAppObservabilityPM2Tasks(TaskSet):
    @task(1)
    def health_check(self):
        response = self.client.get("/health-check")
        assert response.status_code == 200, f"Health check failed with {response.status_code}"

    @task(2)
    def about(self):
        response = self.client.get("/about")  # Replace with your endpoint
        assert response.status_code == 200, f"About failed with with {response.status_code}"

    @task(3)
    def home(self):
        response = self.client.get("/")  # Replace with actual payload
        assert response.status_code == 200, f"Home failed with {response.status_code}"

    @task(4)
    def custom(self):
        response = self.client.get("/custom")  # Replace with actual payload
        assert response.status_code == 200, f"Custom failed with {response.status_code}"

    @task(6)
    def actuator_info(self):
        response = self.client.get("/actuator/info")
        assert response.status_code == 200, f"/actuator/info failed with {response.status_code}"

    @task(6)
    def actuator_info(self):
        response = self.client.get("/actuator/info")
        assert response.status_code == 200, f"/actuator/info failed with {response.status_code}"

    @task(7)
    def actuator_health(self):
        response = self.client.get("/actuator/health")
        assert response.status_code == 200, f"/actuator/health failed with {response.status_code}"

    @task(8)
    def metrics(self):
        response = self.client.get("/metrics")
        assert response.status_code == 200, f"/metrics failed with {response.status_code}"


# Define users for the first app
class NodeAppObservabilityUser(HttpUser):
    tasks = [NodeAppObservabilityTasks]
    host = "http://localhost:30001"  # Replace with your app's base URL
    wait_time = between(1, 3)  # Simulate user wait time between 1 and 3 seconds


# Define users for the second app
class NodeAppObservabilityPM2User(HttpUser):
    tasks = [NodeAppObservabilityPM2Tasks]
    host = "http://localhost:30002"  # Replace with your second app's base URL
    wait_time = between(1, 3)  # Simulate user wait time between 1 and 3 seconds
