def result(n):
    password = ''
    x = 0
    y = 0
    for x in range(n - 1):
        for y in range(n):
            if x + y == n:
                password += str(x) + str(y) + ' '
            else:
                continue
    return password

n = int(input("Введите первое число: "))
print(f'Все варианты пароля по парно {result(n)}')
