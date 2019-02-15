a = int(input())
b = [input().lower().split() for i in range(a)]
_dict = []
for i in range(len(b)):
    _dict += b[i]
c = int(input())
d = [input().split() for j in range(c)]
result = []
for row in range(len(d)):
    for col in range(len(d[row])):
        if d[row][col].lower() in _dict:
            continue
        else:
            if d[row][col] not in result:
                result.append(d[row][col])
[print(i) for i in result]
