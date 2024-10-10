class FactorialCalculate:

    def fa_calc(self, x):
        if x == 1:
            return 1
        else:
            return x * self.fa_calc(x - 1)
print("Hello!\nI'm the Factorial calculating function with recursion algorithm\n")
a = int(input("Enter the number to calculate it factorial: "))
f = FactorialCalculate()
print(f"The factorial of {a} is",f.fa_calc(a))