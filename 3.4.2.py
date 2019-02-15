_max = 0
d = {}

with open("C:\\Users\\DPronkin\\Downloads\\dataset_3363_3.txt") as inf:
    for line in inf:
        line = line.lower().split(' ')
        for x in line:
            if x not in d:
                d[x] = 1
            else:
                d[x] = (d[x] + 1)
        for value in d.values():
            if value >= _max:
                _max = value
result = []
for key, value in d.items():
    if value == _max:
        result.append([key, value])
print((sorted(result))[0][0], (sorted(result))[0][1], end=" ")



