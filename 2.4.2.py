string = input()
count = 0
new_string = ""
if len(string) == 1:
    print(string + str(1))
for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        count += 1
    else:
        count += 1
        new_string += string[i - 1] + str(count)
        count = 0
    if i == len(string) - 1:
        count += 1
        new_string += string[i] + str(count)
print(new_string)
