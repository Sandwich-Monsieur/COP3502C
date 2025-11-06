from functions import *
import unittest


class TestRemoveVowels(unittest.TestCase):
    # all/some/none/empty/y
    def test_remove_lower_vowels(self):
        self.assertEqual(remove_vowels("aeiou"), "")

    def test_remove_upper_vowels(self):
        self.assertEqual(remove_vowels("AEIOU"), "")

    def test_remove_some_vowels(self):
        self.assertEqual(remove_vowels("hello world"), "hll wrld")

    def test_no_vowels(self):
        self.assertEqual(remove_vowels("rhythm"), "rhythm")

    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_y_vowel(self):
        self.assertEqual(remove_vowels("y"), "y")

class TestPrime(unittest.TestCase):
    #prime/even/1/large/negative
    def test_prime_number(self):
        self.assertTrue(is_prime(7))

    def test_non_prime_even(self):
        self.assertFalse(is_prime(8))

    def test_non_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_prime_large(self):
        self.assertTrue(is_prime(97))

    def test_negative_number(self):
        self.assertFalse(is_prime(-5))

if __name__ == "__main__":
    unittest.main()
