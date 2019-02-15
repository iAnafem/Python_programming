def f(num):
    return num


n = int(input())
_dict = {}
array = [int(input()) for i in range(n)]

for x in array:
    if x in _dict:
        print(_dict[x])
    else:
        _dict[x] = f(x)
        print(_dict[x])

