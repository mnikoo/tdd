import unittest
import string_processing

class TestStringProcessing(unittest.TestCase):

    def test_reverse_symmetric(self):
        self.assertEqual(string_processing.reverse_string("ABBA"), "ABBA")

    def test_reverse_asymmetric(self):
        self.assertEqual(string_processing.reverse_string("ABC"), "CBA")

    def test_reverse_empty_string(self):
        self.assertEqual(string_processing.reverse_string(""), "")

    def test_reverse_one_character(self):
        self.assertEqual(string_processing.reverse_string("Z"), "Z")

    def test_reverse_one_character(self):
        self.assertEqual(string_processing.reverse_string(None), None)

    def test_reverse_sentence(self):
        self.assertEqual(string_processing.reverse_sentence("Hello World"), "World Hello")

    def test_reverse_sentence(self):
        self.assertEqual(string_processing.reverse_sentence("This is a test"), "test a is This")

    def test_reverse_empty_sentence(self):
        self.assertEqual(string_processing.reverse_sentence(""), "")

    def test_reverse_empty_sentence(self):
        self.assertEqual(string_processing.reverse_sentence(None), None)