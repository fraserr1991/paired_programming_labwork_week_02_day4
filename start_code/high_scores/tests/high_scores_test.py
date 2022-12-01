import unittest

from src.high_scores import get_latest_score, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [100, 0, 90, 30]
    
    # Tests

    # Test latest score (the last thing in the list)

    def test_latest_score(self):
        latest_score = get_latest_score(self.scores)
        self.assertEqual(30, latest_score)

    # Test personal best (the highest score in the list)
    
    def test_personal_best(self):
        pb = personal_best(self.scores)
        self.assertEqual(100, pb)


    # Test top three from list of scores

    def test_personal_top_three(self):
        top_three = personal_top_three(self.scores)
        self.assertEqual([100, 90, 30], top_three)

    # Test ordered from highest to lowest

    def test_scores_highest_to_lowest(self):
        high_to_low = personal_top_three(self.scores)
        self.assertEqual([100, 90, 30, 0], high_to_low)

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
