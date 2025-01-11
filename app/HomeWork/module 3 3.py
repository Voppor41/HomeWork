def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 4])
values_list = [4, 'hello', False]
values_dict = {"a": "asd", "b": False, "c": 52}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [3, 'io']
print_params(*values_list_2, 42)

