n = int(input())
s = [input().split(";") for i in range(n)]
teams = set()
result = dict()
for i in range(len(s)):
    teams.add(s[i][0])
    teams.add(s[i][2])
for j in teams:
    result[j] = [0] * 5
for match in s:
    if match[1] > match[3]:
        result[match[0]][0] += 1
        result[match[0]][1] += 1
        result[match[0]][4] += 3
        result[match[2]][0] += 1
        result[match[2]][3] += 1
    elif match[1] < match[3]:
        result[match[2]][0] += 1
        result[match[2]][1] += 1
        result[match[2]][4] += 3
        result[match[0]][0] += 1
        result[match[0]][3] += 1
    elif match[1] == match[3]:
        result[match[2]][0] += 1
        result[match[2]][2] += 1
        result[match[2]][4] += 1
        result[match[0]][4] += 1
        result[match[0]][0] += 1
        result[match[0]][2] += 1
for x in result:
    print(x, end=":")
    for y in range(len(result[x])):
        print(result[x][y], end=" ")
    print()
