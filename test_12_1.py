import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner1 = Runner('John Snown')
        for count1 in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner2 = Runner('Oliver Jackson')
        for count2 in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner3 = Runner('Naruto')
        runner4 = Runner('Saske')
        for count3 in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)

if __name__ == "__main__":
    unittest.main()
