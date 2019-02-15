_str = ''
array = []
while True:
    _str = str(input()) # ввод строк
    if _str == 'end':
        break
    array.append([int(s) for s in _str.split()])
li, lj = len(array), len(array[0])
new = [[sum([array[i-1][j], array[(i+1) % li][j], array[i][j-1], array[i][(j+1) % lj]])
        for j in range(lj)] for i in range(li)]

for i in range(li):
    for j in range(lj):
        print(new[i][j], end=' ')
    print()
