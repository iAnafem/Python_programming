array = [int(i) for i in input().split()]
array.sort()
result = []
if len(array) == 1:
    print("")
else:
    for j in array:
        if array.count(j) >= 2:
            if j not in result:
                result.append(j)
            array.remove(j)
for x in result:
    print(x, end=" ")

