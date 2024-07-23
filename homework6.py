my_dict = {'Egor': 2005, 'Denis': 1999, 'Polina': 2007}
print(my_dict)
print(my_dict['Egor'])
print(my_dict.get('Vika'))
my_dict.update({'Kamila': 2000,
                'Max': 1979})
a = my_dict.pop('Egor')
print(a)
print(my_dict)
print()

my_set = {1, 2, 4, '9', 2, False, '8', '9'}
print(my_set)
my_set.add(5)
my_set.add('Hello')
my_set.remove('9')
print(my_set)

