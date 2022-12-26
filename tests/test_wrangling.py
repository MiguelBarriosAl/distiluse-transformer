import unittest

from app.wrangling import clean_text, split_text


class TestWrangling(unittest.TestCase):
    def test_clean_text(self):
        text = "$AaBbWw{_Zz1234*"
        response = clean_text(text)
        self.assertEqual(response, "AaBbWw  Zz1234")

    def test_n_split_text(self):
        text1 = "TESTING.Doing unit tests on Wrangling functions. Knowing the behaviour of functions"
        text2 = "Doing unit tests on Wrangling functions, Knowing the behaviour of functions"
        response1 = split_text(text1, 512)
        response2 = split_text(text1, 1512)
        response3 = split_text(text2, 512)
        self.assertEqual(len(response1), 2)
        self.assertEqual(len(response2), 3)
        self.assertEqual(len(response3), 2)

    def test_split_text(self):
        text = "Testing,demo_1"
        response = split_text(text, 512)
        out_text = ["Testing", "demo_1"]
        self.assertEqual(response, out_text)
