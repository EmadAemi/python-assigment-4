a = int(input("a: "))
b = int(input("b: "))
if a > b: a, b = b, a
for i in range(b, a*b+1):
    if i % a == 0 and i % b == 0:
        print("kmm", i)
        break
