a = int(input())
b = a
result = a ** 2
while b != 0:
    a = int(input())
    b += a
    result += a ** 2
    if b == 0:
        break
print(result)
