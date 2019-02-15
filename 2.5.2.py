array = [int(i) for i in input().split()]
result = []
if len(array) == 1:
    print(array[0])
else:
    for j in range(len(array) - 1):
        result.append(array[j - 1] + array[j + 1])

    result.append(array[-2] + array[0])
    for x in result:
        print(x, end=" ")

