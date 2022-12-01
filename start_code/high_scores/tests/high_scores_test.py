import unittest

from src.high_scores import get_latest_score, personal_best, personal_top_three, highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [100, 0, 90, 30]
        self.scores_2 = [100, 100, 50, 90, 0, 10]

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
        high_to_low = highest_to_lowest(self.scores)
        self.assertEqual([100, 90, 30, 0], high_to_low)

    # Test top three when there is a tie
    def test_tie(self):
        score = [50, 100, 100, 75, 10]
        top_scores = personal_top_three(score)    
        self.assertEqual([100,100,75], top_scores)

    # Test top three when there are less than three

    def test_list_less_than_three(self):
        score = [50,100]
        top_scores = personal_top_three(score)
        self.assertEqual([100,50], top_scores)

    # Test top three when there is only one
    def test_list_only_one(self):
        score = [50]
        only_one = personal_top_three(score)
        self.assertEqual([50], only_one)
    
