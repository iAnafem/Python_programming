a = int(input())
b = int(input())
c = int(input())
d = int(input())


for i in range(c, d + 1):
    print(' \t', i, end='')
for x in range(a, b + 1):
    print('\n', x, end='\t')
    for y in range(c, d + 1):
        print(x * y, end='\t')

