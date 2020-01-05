import unittest
from beer import beer


class TestBeer(unittest.TestCase):
    def test_beer(self):
        patterns = [
            (99, '99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, 98 bottles of beer on the wall.\n'),
            (2, '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n'),
            (1, '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n')
        ]

        for n, expected in patterns:
            with self.subTest(n):
                self.assertEqual(beer(n), expected)


if __name__ == '__main__':
    unittest.main()