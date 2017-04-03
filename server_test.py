import unittest

from server import app

SUCCESS = 200
MOVED = 301
NOT_FOUND = 404


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()

    def test_root(self):
        self.assertEqual(
            self.test_client.get('/').status_code,
            NOT_FOUND)

    def test_askme(self):
        self.assertEqual(
            self.test_client.get('/askmeanything').status_code,
            MOVED)

    def test_question(self):
        self.assertEqual(
            self.test_client.get('/askmeanything/?q=Hello').status_code,
            SUCCESS)


if __name__ == '__main__':
    unittest.main()
