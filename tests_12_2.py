import module_12_runner
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen,  'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run_1 = module_12_runner.Runner('Усэйн', 10)
        self.run_2 = module_12_runner.Runner('Андрей', 9)
        self.run_3 = module_12_runner.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r_1 = module_12_runner.Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_results = module_12_runner.Tournament.start(r_1)
        print(self.all_results)
        print(self.assertTrue(max(self.all_results), 'Ник'))
        # return self.all_results
    #
    # def assertTrue(self, expr, msg = None):


    @classmethod
    def tearDownClass(cls):
        print(cls.all_results, '\n')


    # def test_walk(self):
    #     for i in range(10):
    #         module_12_runner.Runner.walk(run_1)