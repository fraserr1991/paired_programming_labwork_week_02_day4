import unittest
from src.phone_number import * 

class TestPhoneNumber(unittest.TestCase):
   
    def setUp(self):
        self.phone_number_1 = 1234567890

    def test_string(self):
        test_string = change_int_to_new_string(self.phone_number_1)
        self.assertEqual("(123) 456-7890", test_string)
