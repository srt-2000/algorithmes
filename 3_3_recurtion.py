class KeyFinder:
    def find_key(self, box_list, n_key):
        if n_key in box_list:
            return box.index(key)
        else:
            return self.find_key(box, key)

print("Hello!\nI'm the finder of KEY list's position with recursion algorithm.")
box = [int(n) for n in input("\nEnter the list numbers you want to create:").split()]
key = int(input("\nEnter the number you want to find position:"))
f = KeyFinder()
print(f"The position of {key} is:",f.find_key(box, key))