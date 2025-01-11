import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Создаем общий словарь для хранения результатов всех тестов
        cls.all_results = {}

    def setUp(self):
        # Создаем участников для тестов
        self.runner_usain = Runner('Усэйн', 10)
        self.runner_andrey = Runner('Андрей', 9)
        self.runner_nick = Runner('Ник', 3)

    def test_race_usain_and_nick(self):
        # Забег с Усэйном и Ником
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()

        # Проверяем, что последний финишировавший — Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник', 'Ник должен быть последним')

        # Сохраняем результаты в общий словарь
        TournamentTest.all_results['test_race_usain_and_nick'] = results

    def test_race_andrey_and_nick(self):
        # Забег с Андреем и Ником
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()

        # Проверяем, что последний финишировавший — Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник', 'Ник должен быть последним')

        # Сохраняем результаты в общий словарь
        TournamentTest.all_results['test_race_andrey_and_nick'] = results

    def test_race_usain_andrey_and_nick(self):
        # Забег с Усэйном, Андреем и Ником
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()

        # Проверяем, что последний финишировавший — Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник', 'Ник должен быть последним')

        # Сохраняем результаты в общий словарь
        TournamentTest.all_results['test_race_usain_andrey_and_nick'] = results

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты всех тестов в столбец
        print("\nВсе результаты тестов:")
        for test_name, result in cls.all_results.items():
            print(f"\nРезультаты для {test_name}:")
            # Сортируем результат по месту (ключу) и выводим по порядку
            for place, runner in sorted(result.items()):
                print(f"  Место {place}: {runner.name}")

