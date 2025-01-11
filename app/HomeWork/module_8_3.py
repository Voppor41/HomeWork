class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:

    def __init__(self, model, vin, number):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.number = self.__is_valid_number(number)

    def __is_valid_vin(self, vin_number):

        if not (isinstance(vin_number, int)):
            print(IncorrectVinNumber('Некорректный тип vin номера'))
        else:
            if 1000000 <= vin_number <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_number(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        else:
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
