import unittest
from src.app.checkers import test_allowed_file


class TestFile(unittest.TestCase):
    def test_allowed_file(self):
        file = 'test-file.csv'
        test_allowed_file(file)
        message = "Test test_allowed_file value is not true"
        self.assertTrue(test_allowed_file(file), message)


if __name__ == 'main':
    unittest.main()
