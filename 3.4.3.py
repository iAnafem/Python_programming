with open("C:\\Users\\DPronkin\\Downloads\\dataset_3363_4.txt", 'r') as lst:
    grades = [0] * 3
    count = 0
    _str = [line.strip().split(";") for line in lst]
    [print(i) for i in [float((int(math) + int(phys) + int(lang)) / 3) for name, math, phys, lang in _str]]
    sum_math = 0
    sum_phys = 0
    sum_lang = 0
    for i in range(len(_str)):
        sum_math += int(_str[i][1])
        sum_phys += int(_str[i][2])
        sum_lang += int(_str[i][3])
    print(sum_math / len(_str), sum_phys / len(_str), sum_lang / len(_str), end=" ")

