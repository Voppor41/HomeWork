import unittest
from runner_and_tournament import Runner, Tournament


def freeze_check(func):
    def wrapper(self, *args, **kwargs):
        # Проверка значения is_frozen
        if self.is_frozen:
            # Пропуск теста с помощью unittest.skip
            @unittest.skip("Тесты в этом кейсе заморожены")
            def skipped_test(*args, **kwargs):
                pass

            return skipped_test(self, *args, **kwargs)
        else:
            return func(self, *args, **kwargs)

    return wrapper

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @freeze_check
    def test_walk(self):
        runner1 = Runner('John Snown')
        for count1 in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @freeze_check
    def test_run(self):
        runner2 = Runner('Oliver Jackson')
        for count2 in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    @freeze_check
    def test_challenge(self):
        runner3 = Runner('Naruto')
        runner4 = Runner('Saske')
        for count3 in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        # Создаем общий словарь для хранения результатов всех тестов
        cls.all_results = {}

    @freeze_check
    def setUp(self):
        # Создаем участников для тестов
        self.runner_usain = Runner('Усэйн', 10)
        self.runner_andrey = Runner('Андрей', 9)
        self.runner_nick = Runner('Ник', 3)

    @freeze_check
    def test_race_usain_and_nick(self):
        # Забег с Усэйном и Ником
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()

        # Проверяем, что последний финишировавший — Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник', 'Ник должен быть последним')

        # Сохраняем результаты в общий словарь
        TournamentTest.all_results['test_race_usain_and_nick'] = results

    @freeze_check
    def test_race_andrey_and_nick(self):
        # Забег с Андреем и Ником
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()

        # Проверяем, что последний финишировавший — Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник', 'Ник должен быть последним')

        # Сохраняем результаты в общий словарь
        TournamentTest.all_results['test_race_andrey_and_nick'] = results

    @freeze_check
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

