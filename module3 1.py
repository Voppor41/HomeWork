def count_calls():
    global calls
    calls += 1

def string_info(string: str):
    count_calls()
    str_tuple = tuple(string)
    return len(str_tuple), string.upper(), string.lower()


def is_contains(string: str, lst: list):
    count_calls()
    for i in range(len(lst)):
        lst[i] = str.casefold(lst[i])

    if string.casefold() in lst:
        return True
    else:
        return False


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
