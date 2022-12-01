import unittest
from src.word_reverser import *

class TestWordReverse(unittest.TestCase):
    
    # Have unit tests for the following sentences 
    def test_first_sentence(self):
        first_sentence_reversed = reverse_word("Hey fellow warriors")
        self.assertEquals("Hey wollef sroirraw", first_sentence_reversed)

    def test_second_sentence(self):
        second_sentence_reversed = reverse_word("This is a test")
        self.assertEquals("This is a test", second_sentence_reversed)
    
    def test_third_sentence(self):
        third_sentence_reversed = reverse_word("This is another test")
        self.assertEquals("This is rehtona test", third_sentence_reversed)        
    # "Hello this is a test, fantastic"
    # "The cat was cute and he was called Azzazel"
    # "Very cool hat"

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"
