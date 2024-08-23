def count_result(data):
    numbers = []
    strings = []
    trash = []

    def help(item):
        if isinstance(item, int) or isinstance(item, float):
            numbers.append(item)
        elif isinstance(item, str):
            strings.append(item)
        elif isinstance(item, list) or isinstance(item, tuple):
            for sub_item in item:
                help(sub_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                help(key)
                help(value)
        else:
            trash.append(item)

    help(data)

    count_numbers = 0
    for i in numbers:
        count_numbers += i
    count_string = 0
    for i in strings:
        count_string += len(i)
    return count_numbers + count_string


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(count_result(data_structure))