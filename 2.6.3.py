lst = [int(i) for i in input().split()]
x = int(input())
for num in range(len(lst)):
    if lst[num] == x:
        print(num, end=" ")
if x not in lst:
    print("Отсутствует", end=" ")





