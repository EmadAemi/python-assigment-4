from math import sqrt

print("ax^2 + bx + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
delta = b ** 2 - 4 * a * c
if delta < 0: print("No root")
elif delta == 0: print((-1)*b / (2*a))
else: print(((-1)*b-sqrt(delta)) / (2*a), ((-1)*b+sqrt(delta)) / (2*a))
