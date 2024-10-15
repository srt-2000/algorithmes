import json

class WordFinder:

    def __init__(self):
        self.word_table = {}
        self.word = None

    def find_world(self, word, word_table):
        self.word = word
        self.word_table = word_table
        if self.word in self.word_table:
            print("this world is on page -", self.word_table[self.word])
        if self.word not in self.word_table:
            print("there is no this word on our pages, sorry")

with open("data/11_2_data.json", "r") as file:
    inv_hash = json.load(file)

a = "hi there"
b = "hi adit"
c = "there we go"

print(f"Hi, I'm inverted index algorithm. We have \npage a with phrase:{a}\npage b with phrase:{b}\npage c with phrase:{c}")
d = input("Input word from phrases and fin the pages:")
f = WordFinder()
f.find_world(d, inv_hash)