n = int(input())
move = []
right, up = 0, 0
while n > 0:
    move.append(input().split())
    n -= 1
for i in range(len(move)):
    if move[i][0] == "север":
        up += int(move[i][1])
    elif move[i][0] == "юг":
        up -= int(move[i][1])
    elif move[i][0] == "восток":
        right += int(move[i][1])
    elif move[i][0] == "запад":
        right -= int(move[i][1])
print(right, up, end=" ")
