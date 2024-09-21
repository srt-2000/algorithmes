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


'''
def multiple_matrix(arr):
    b = arr
    matrix = []
    for i in arr:
        c = []
        for j in b:
            c.append(i * j)
        matrix.append(c)
    return matrix
print(multiple_matrix([1, 2, 3]))

def mul_mat(arr):
    b = {}
    matrix = []
    for i in arr:
        b[i] = [x * i for x in arr]
        matrix.append(b[i])
    return matrix

print(mul_mat([1, 2, 3]))
'''