with open("D:\\Книги\\dataset_3380_5.txt") as f:
    _result = {}
    lines = []
    for line in f:
        lines.append(line.strip().split())
    for i in range(1, 12):
        _result[i] = []
        for name in range(len(lines)):
            if int(lines[name][0]) == i:
                _result[i].append(int(lines[name][2]))
    for key in _result:
        if _result[key] is not None:
            print(key, sum(_result[key]) / len(_result[key]), end=" ")
        else:
            print(key, "-", end=" ")
        print()
