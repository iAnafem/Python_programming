def gcd(a, b):
    assert a >= 0 and b >= 0
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


num1 = int(input())
num2 = int(input())
print(int(num1 * num2 / gcd(num1, num2)))
