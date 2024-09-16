class WordsFinder:

    def __init__(self, *files):
        self.files = files

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.files:
            with open(file_name, 'r', encoding="utf-8") as f:
                text = f.read().lower()
                for p in punctuation:
                    text = text.replace(p, ' ')
                words = text.split()
                all_words[f.name] = words
        return all_words

    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower()) + 1  # Позиция слова (1-based index)
                result[file_name] = position
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.get_all_words())  #  Все слова
