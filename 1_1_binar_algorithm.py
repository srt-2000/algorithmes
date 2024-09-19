class PositionFinder:
    def __init__(self):
        self.max_list = None
        self.low = 0

    def bin_search(self, range_list, find_x):
        print("\nWhen I start to reduce our range for half's and try to find there:")
        self.max_list = len(range_list) - 1
        while self.low <= self.max_list:
            mid = int((self.low + self.max_list) / 2)
            guess = range_list[mid]
            print("Try range from position", self.low, "to position", self.max_list)
            if guess == find_x:
                return mid
            elif guess > find_x:
                self.max_list = mid - 1
            else:
                self.low = mid + 1
        return None

print("Hello!\nI'm a very very fast algorithm for searching on sorted range.\nI'm the binary search algorithm.")
m = int(input("Enter the maximum number of sorted array:"))
x = int(input("Enter the digit we want to find:"))

my_list = [n for n in range(1, m + 1)]
print("\nFirst of all I create a sorted list for your range:\n", my_list)

position = PositionFinder()
print("\nFIND!!!\n", position.bin_search(my_list, x), "is position of", x)