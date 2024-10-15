import functools
import json


class RedFun:

    def __init__(self):
        self.lst = []

    def arr_sum(self, lst):
        self.lst = lst
        return functools.reduce(lambda a, b: a + b, self.lst)

    def arr_max(self, lst):
        self.lst = lst
        return functools.reduce(lambda a, b: a if a > b else b, self.lst)

with open("data/11_5_data.json", "r") as file:
    test_list = json.load(file)
l = RedFun()

print(f"A functools.reduce function.\nWe have an array:{test_list}")
print(f"The sum of elements in test_list is:{l.arr_sum(test_list)}")
print(f"The maximum element in test_list is:{l.arr_max(test_list)}")