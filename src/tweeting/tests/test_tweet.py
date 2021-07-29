import unittest

from tweeting import tweet


class TestCase(unittest.TestCase):
    def test_dump(self):
        self.assertTrue(tweet._stub())


if __name__ == '__main__':
    unittest.main()
