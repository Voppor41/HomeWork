def add_everything_up(a: [int, float, str], b: [int, float, str]):
    try:
        c = a + b
    except TypeError as exc:
        return str(a)+str(b)
    else:
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
