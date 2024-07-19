example = 'Топинамбур'
b = ''
print(example[0])
print(example[-1])
print(example[5::])
print(example[::-1])

for i in range(len(example)):
    if i != 0 and i % 2 != 0:
        b += example[i]

print(b)
