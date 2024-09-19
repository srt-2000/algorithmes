import functools

test_list = [1, 4, 5, 3, 6, 8, 2, 9, 12, 3, 56, 1, 4, 89, 34, 4, 6, 4, 5, 7]

print("The sum of elements in test_list is:", end="")
print(functools.reduce(lambda a, b: a + b, test_list))

print("The maximum element in test_list is:", end="")
print(functools.reduce(lambda a, b: a if a > b else b, test_list))