class QuickSort:
    def sorted(self, arr):
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[int(len(arr) / 2)]
            less = [i for i in arr if i < pivot]
            greater = [i for i in arr if i > pivot]
            return self.sorted(less) + [pivot] + self.sorted(greater)

print("Hello!\nI'm the quick sort function with recursion algorithm.")
a = [int(n) for n in input("\nEnter the list you want to sort:").split()]
b = QuickSort()
print(f"Here is your sorted array:", b.sorted(a))