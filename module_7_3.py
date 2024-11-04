from os import replace


class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}

        for i in self.file_names:
            with open(i, encoding='UTF-8') as f_1:
                line_1 = str(f_1.readlines()).lower()
                punkt_1 = ["[",'.', '=', '!',';', ':', ' - ', ",", "'",  "]",'"']
                for k in punkt_1:
                    line_1 = line_1.replace(k,"")

                # print (line_1)

                ww_1 = line_1.split()
                all_words[i] = ww_1

                continue
        return all_words

    def find(self, word):
        new_dict ={}
        for key, words in self.get_all_words().items():
            for i in words:
                if i == word.lower():
                    new_dict[key] = words.index(i)+1
                    # print(new_dict)
        return new_dict


    def count(self, word):
        new_dict1 = {}

        for key, words in self.get_all_words().items():
            j = 0
            for i in words:
                if i == word.lower():
                    j+=1

            new_dict1[key] = j

        return new_dict1

finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего