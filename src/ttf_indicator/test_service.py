import unittest
from fastapi.testclient import TestClient
from ttf_indicator.service import app, state

class TestService(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        # Reset state before each test
        state.clear()
        state["past"] = [{"state": 5.6}, {"state": 15}]

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "OK")

    def test_register_new_user(self):
        response = self.client.post("/newuser")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "user created")
        self.assertIn("newuser", state)
        self.assertEqual(state["newuser"], [])

    def test_add_new_indicator(self):
        response = self.client.post("/past/indicators")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 2)

    def test_add_indicator_user_not_found(self):
        response = self.client.post("/nonexistent/indicators")
        self.assertEqual(response.status_code, 404)

    def test_get_indicator(self):
        response = self.client.get("/past/indicators/0")
        self.assertEqual(response.status_code, 200)

    def test_get_indicator_not_found(self):
        response = self.client.get("/past/indicators/99")
        self.assertEqual(response.status_code, 404)

    def test_update_indicator(self):
        response = self.client.put("/past/indicators/0?ttf=10.5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(state["past"][0]["state"], 10.5)

    def test_update_indicator_user_not_found(self):
        response = self.client.put("/nonexistent/indicators/0?ttf=10.5")
        self.assertEqual(response.status_code, 404)

    def test_update_indicator_sensor_not_found(self):
        response = self.client.put("/past/indicators/99?ttf=10.5")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()