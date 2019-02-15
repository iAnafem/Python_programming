string = input()
print((string.upper().count('G'.upper()) + string.upper().count('C'.upper())) * 100 / len(string))
