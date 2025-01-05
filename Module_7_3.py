class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        positions = {}
        for name, words in all_words.items():
            try:
                position = words.index(word) + 1
                positions[name] = position
            except ValueError:
                positions[name] = None
        return positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        counts = {}
        for name, words in all_words.items():
            counts[name] = words.count(word)
        return counts


with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("It's a text for task Найти везде,\nИспользуйте его для самопроверки.\nУспехов в решении задачи!\ntext text text")

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
