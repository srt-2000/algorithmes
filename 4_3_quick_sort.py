class MultipleMatrix:

    def __init__(self):
        self.b = {}
        self.matrix = []

    def mult_matrix(self, arr):
        for i in arr:
            self.b[i] = [x * i for x in arr]
            self.matrix.append(self.b[i])
        return self.matrix

print("Hello!\nI'm the multiplication array function.")
a = [int(n) for n in input("\nEnter the array you want to multiplicate with itself:").split()]
b = MultipleMatrix()
print(f"Here is your multiplicated matrix:", b.mult_matrix(a))