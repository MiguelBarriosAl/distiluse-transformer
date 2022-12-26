import unittest
from unittest import mock
from src.app.checkers import check_allowed_file, check_n_tokens


class TestCheckers(unittest.TestCase):
    def test_allowed_file(self):
        file = "test-file.txt"
        check_allowed_file(file)
        message = "Test test_allowed_file value is not true"
        self.assertTrue(check_allowed_file(file), message)

    @mock.patch("src.app.checkers.n_tokens")
    def test_check_n_tokens_512(self, mock_response):
        mock_response.return_value = 513
        response = check_n_tokens("Gestion del.Impuesto")
        self.assertEqual(response, ["Gestion del", "Impuesto"])

    @mock.patch("src.app.checkers.n_tokens")
    def test_check_n_tokens_50(self, mock_response):
        mock_response.return_value = 49
        response = check_n_tokens("Gestion del.Impuesto")
        self.assertEqual(response, [])

    @mock.patch("src.app.checkers.n_tokens")
    def test_check_n_tokens_100(self, mock_response):
        mock_response.return_value = 100
        response = check_n_tokens("Gestion del.Impuesto")
        self.assertEqual(response, ["Gestion del.Impuesto"])


if __name__ == 'main':
    unittest.main()
