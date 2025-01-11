import unittest
import test_12_3


testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
