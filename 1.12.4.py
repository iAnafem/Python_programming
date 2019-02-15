item = input()
if item == "треугольник":
    a, b, c = (int(input()) for i in range(3))
    print((((a + b + c) / 2) * (((a + b + c) / 2) - a) * (((a + b + c) / 2) - b) *
           (((a + b + c) / 2) - c)) ** 0.5)
elif item == "прямоугольник":
    a, b = tuple(int(input()) for i in range(2))
    print(a * b)
elif item == "круг":
    print(3.14 * int(input()) ** 2)
