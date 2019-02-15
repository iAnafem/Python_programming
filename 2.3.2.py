a, b = int(input()), int(input())
numbers = 0
q = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        numbers += i
        q += 1
print(float(numbers / q))
