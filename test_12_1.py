

import module_12_runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run_1 = module_12_runner.Runner('Иван')
        for i in range(10):
            module_12_runner.Runner.walk(run_1)

        # print(run_1.distance)
        self.assertEqual(run_1.distance, 50)
        # return run_1.distance

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_2 = module_12_runner.Runner('Марья')
        for i in range(10):
            module_12_runner.Runner.run(run_2)

        print(run_2.distance)
        self.assertEqual(run_2.distance, 70)
        return run_2.distance

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_1 = module_12_runner.Runner('Иван')
        run_2 = module_12_runner.Runner('Марья')
        for i in range(10):
            module_12_runner.Runner.walk(run_1)
            module_12_runner.Runner.run(run_2)


        print( run_1.distance, run_2.distance)
        self.assertNotEqual(run_1.distance, run_2.distance)
        return run_1.distance, run_2.distance