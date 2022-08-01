a = int(input("a: "))
b = int(input("b: "))
if a > b: a, b = b, a
for i in reversed(range(a)):
    if a % i == 0 and b % i == 0:
        print("bmm", i)
        break
