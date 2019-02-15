_seq = [[num] * int(num) for num in range(1, 1000)]
limit = int(input())
count = 0

for i in range(len(_seq)):
    for j in range(len(_seq[i])):
        count += 1
        if count > limit:
            break
        print(_seq[i][j], end=" ")
    if count > limit:
        break
