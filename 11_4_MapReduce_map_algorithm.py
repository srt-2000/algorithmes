class Sqr:

    def __init__(self):
        self.result = None

    def sqr_arr(self, a_):
        self.result = map(lambda x: x ** 2, a_)
        return list(self.result)

a = [1, 2, 3 , 4, 5]
b = Sqr()
print(f"A map function.\nWe have an array:{a}\nAnd we've powered every element:{b.sqr_arr(a)}")