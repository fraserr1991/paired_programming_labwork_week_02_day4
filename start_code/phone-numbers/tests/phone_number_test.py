import unittest
from src.phone_number import * 

class TestPhoneNumber(unittest.TestCase):
   
    def setUp(self):
        self.phone_number_1 = 1234567890

    def test_is_converted_to_string(self):
        converted_string = convert_integer_to_string(self.phone_number_1)
        self.assertEqual("1234567890",  converted_string)

    def test_split_string_one(self):
        section_one = create_section_one("1234567890")
        self.assertEqual("123", section_one)

    def test_split_string_two(self):
        section_two = create_section_two("1234567890")
        self.assertEqual("456", section_two)
    
    def test_split_string_three(self):
        section_three = create_section_three("1234567890")
        self.assertEqual("7890", section_three)    

    def test_string_concatenation(self):
        final_string = concatenate_strings("123", "456", "7890")
        self.assertEqual("(123) 456-7890", final_string)

    def test_create_phone_number(self):
        phone_number = create_phone_number(self.phone_number_1)
        self.assertEqual("(123) 456-7890", phone_number)