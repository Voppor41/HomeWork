import unittest
from rt_with_exceptions import Runner
import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    format="%(asctime)s | %(levelname)s | %(message)s", encoding="UTF-8")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner1 = Runner('John Snow')
            for count1 in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('test_walk was completed successfully', exc_info=True)
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner2 = Runner(22)
            for count2 in range(10):
                runner2.run()
            self.assertEqual(runner2.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner3 = Runner('Naruto')
        runner4 = Runner('Saske')
        for count3 in range(10):
            runner3.walk()
            runner4.run()
        self.assertNotEqual(runner3.distance, runner4.distance)
        logging.info("test_challenge выполнен успешно")

if __name__ == '__main__':
    unittest.main()
