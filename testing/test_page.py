from unittest import TestCase
from unittest.mock import patch
from testing.page import PageRequest


class TestPageRequest(TestCase):
    def setUp(self) -> None:
        self.page = PageRequest("https:google.com")

    def test_make_request(self):
        with patch("requests.get") as mocked_get:
            self.page.get()
            mocked_get.assert_called()

    def test_content_return(self):
        fake_content = "Hello"

        class FaleResponse:
            def __init__(self):
                self.content = fake_content

        with patch("requests.get", return_value=FaleResponse()) as mocked_get:
            result = self.page.get()
            self.assertEqual(result, fake_content)
