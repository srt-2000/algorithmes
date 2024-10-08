import functools

class RedFun:

    def __init__(self):
        self.lst = []

    def arr_sum(self, lst):
        self.lst = lst
        return functools.reduce(lambda a, b: a + b, self.lst)

    def arr_max(self, lst):
        self.lst = lst
        return functools.reduce(lambda a, b: a if a > b else b, self.lst)

test_list = [1, 4, 5, 3, 6, 8, 2, 9, 12, 3, 56, 1, 4, 89, 34, 4, 6, 4, 5, 7]
l = RedFun()

print(f"A functools.reduce function.\nWe have an array:{test_list}")
print(f"The sum of elements in test_list is:{l.arr_sum(test_list)}")
print(f"The maximum element in test_list is:{l.arr_max(test_list)}")