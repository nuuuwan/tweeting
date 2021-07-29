import unittest

from tweeting import run_tweeting


class TestCase(unittest.TestCase):

    def test_dump(self):
        self.assertTrue(run_tweeting._run())


if __name__ == '__main__':
    unittest.main()
