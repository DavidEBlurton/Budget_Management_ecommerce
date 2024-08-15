import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(solution("nest","I built a nest and tested it"),"here")
    def test_example_two(self):
        self.assertEqual(solution("runs","The dog"),"not here")
    def test_example_three(self):
        self.assertEqual(solution("April","april showers bring may flowers"),"not here")
    def test_find_me(self):
        self.assertEqual(solution("me","me and the homies are gonna go on a picnic"),"here")

        

if __name__ == '__main__':
    unittest.main()