def modify_list(l):
    # put your python code here
    for num in range(len(l) - 1, -1, -1):
        print(num)
        if l[num] % 2 != 0:
            l.pop(num)
        elif l[num] % 2 == 0:
            l[num] //= 2


_list = [1, 2, 3, 4, 5, 6]
modify_list(_list)
print(_list)
modify_list(_list)
print(_list)