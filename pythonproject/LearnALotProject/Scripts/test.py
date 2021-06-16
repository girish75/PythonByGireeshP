import unittest
import randomgame

class MyTestCase(unittest.TestCase):
    def test_game(self):
        lucky_number = rand_start = rand_end = 0
        return_value = randomgame.random_game(lucky_number, rand_start, rand_end)
        self.assertTrue(return_value)

    def test_incorrect(self):
        lucky_number = rand_start = rand_end = None
        return_value = randomgame.random_game(lucky_number, rand_start, rand_end)
        self.assertTrue(return_value)


if __name__ == '__main__':
    unittest.main()
