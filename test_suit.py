import unittest
from unittest import TextTestRunner

import tests_12_2
import test_12_1
# Часть 1
runnST = unittest.TestSuite()
runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnST)


# Часть 2

