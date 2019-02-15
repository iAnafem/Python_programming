_str, _code, encode, decode = (input() for i in range(4))
result1 = ""
result2 = ""
_dict1 = dict(zip(_str, _code))
_dict2 = dict(zip(_code, _str))
for x in encode:
    result1 += _dict1[x]
for y in decode:
    result2 += _dict2[y]
print(result1)
print(result2)

