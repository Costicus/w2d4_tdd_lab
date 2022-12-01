import unittest

from src.high_scores import latest_score, personal_best, personal_top_three, ordered_highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0

    # Tests

    # Test latest score (the last thing in the list)

class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [1000, 1, 500, 233, 7]

    def test_latest_score(self): 
        found_latest_score = latest_score(self.scores)
        self.assertEqual(7, found_latest_score)

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        found_highest_score = personal_best(self.scores)
        self.assertEqual(1000, found_highest_score)

    # Test top three from list of scores
    def test_top_three(self):
        top_three = personal_top_three(self.scores)
        self.assertEqual([1000, 500, 233], top_three)

    # Test ordered from highest to lowest
    def test_highest_to_lowest(self):
        highest_to_lowest = ordered_highest_to_lowest(self.scores)
        self.assertEqual([1000, 500, 233, 7, 1], highest_to_lowest)
    scores = []

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
    
# Your task is to write methods that return the 
# 
# highest score from the list, 
# the last added score 
# and the three highest scores. 