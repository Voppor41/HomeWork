def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 4])
values_list = [4, 'hello', False]
values_dict = {"1": "asd", "2": False, "3": 52}
print_params(*values_dict)
print_params(**values_dict)
values_list2 = [3, 'io']
print_params(*values_list2)

