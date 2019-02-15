n = int(input())
a = [[0] * n for i in range(n)]
b = [[0 for x in range(n)] for y in range(n)]

print(a, b)

a[0][0] = 5
b[0][0] = 4

for item1 in a:
    print(item1)

a, b, c = (int(i) for i in input().split())
print(a, b, c)

