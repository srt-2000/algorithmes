def multi_pl(arr):
    result = 1
    for x in arr:
        result = result * x
    return [result for i in arr]

a = [1, 2, -3]
print(multi_pl(a))
