from math import factorial
a = int(input("N: "))
is_factorial = False
for i in range(a+1):
    if a == factorial(i):
        is_factorial = True
        break
if is_factorial: print("Yes")
else: print("No")