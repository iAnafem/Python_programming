a, b, c = (int(input()) for i in range(3))
_list = [a, b, c]

print(_list.pop(_list.index(max(_list))))
print(_list.pop(_list.index(min(_list))))
print(_list[0])
