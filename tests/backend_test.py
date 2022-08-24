import unittest
import requests


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8000/'
        self.api_session = requests.Session()
        self.api_session.auth = ('admin', 'admin')

    def test_create_user_and_delete(self):

        new_user = {
            "username": "test_user",
            "email": "test@test.com",
            "groups": []
        }

        # Test creating new user
        res = self.api_session.post(self.url + 'users/', data=new_user)
        self.assertEqual(res.status_code, 201)

        new_user_url = res.json()['url']

        # Test the new user exists
        res = self.api_session.get(new_user_url)
        self.assertEqual(res.status_code, 200)

        # Remove the user again
        res = self.api_session.delete(new_user_url)
        self.assertEqual(res.status_code, 204)

    def tearDown(self):
        self.api_session.close()


if __name__ == '__main__':
    unittest.main()
