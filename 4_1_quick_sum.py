class Summator:
    def array_sum(self, arr):
        if not arr:
            return 0
        else:
            return arr.pop(0) + self.array_sum(arr)

print("Hello!\nI'm the sum function with recursion algorithm.")
a = [int(n) for n in input("\nEnter the list numbers you want to summing:").split()]
b = Summator()
print(f"The sum of your array is:", b.array_sum(a))

#original code
'''
def quick_sum(arr):
    if arr == []:
        return 0
    else:
        return arr.pop(0) + quick_sum(arr)
'''