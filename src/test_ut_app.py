import unittest
import app


class test_health_check(unittest.TestCase):
    def test_case1(self):
        resp = app.healthcheck()
        assert resp.status_code == 200

    def test_case2(self):
        resp = app.healthcheck()
        assert resp.get_json() is None


class test_hello(unittest.TestCase):
    def test_case1(self):
        resp = app.hello()
        assert resp.status_code == 200

    def test_case2(self):
        resp = app.hello()
        resp_json = resp.get_json()

        assert resp_json["msg"] == "welcome"

    def test_case3(self):
        resp = app.hello()
        resp_json = resp.get_json()

        assert "test14" not in resp_json


if __name__ == "__main__":
    unittest.main()
