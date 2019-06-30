from utility import get_target_subjects
import unittest

class TestStringMethods(unittest.TestCase):

    def test_get_target_subjects(self):
        tokens = ['BTC', 'is', 'going', 'to', 'the', 'moon']
        subjects = get_target_subjects(tokens)
        self.assertEqual(subjects, ['btc'])

if __name__ == '__main__':
    unittest.main()
