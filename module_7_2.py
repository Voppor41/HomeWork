import io
def custom_write(file_name, strings):
    string_positions = {}
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(len(strings)):
            position = (i+1, f.tell())
            string_positions[position] = strings[i]
            f.write(str(strings[i]) + "\n")
    f.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
