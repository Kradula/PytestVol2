import requests


class TestPost:

    response = None

    def setup_method(self):
        self.response = requests.get("https://jsonplaceholder.typicode.com/posts")

    def test_check_status_code(self, status_code=200):
        assert self.response.status_code == status_code

    def test_is_not_empty(self):
        assert self.response.text != {}

    def test_user_id_is_in_json(self, user_id=1):
        user_ids = [user["userId"] for user in self.response.json() if user["userId"] == 1]
        assert user_id in user_ids

