import re
with open("C:\\Users\\DPronkin\\Downloads\\dataset_3363_2.txt", 'r') as s:
    _str = s.readline().strip()
    a = re.split(r"(\D)", _str)
    print(a)
    result = []
    for i in range(1, len(a), 2):
        print(a[i] * int(a[i + 1]), end='')




