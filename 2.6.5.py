def spiral(n):
    dx, dy = 1, 0
    x, y = 0, 0
    array = [[None] * n for j in range(n)]
    print(array)
    for i in range(1, n ** 2 + 1):
        array[x][y] = i
        print("i = ", i )
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and array[nx][ny] is None:
            x, y = nx, ny
            print("nx = ", nx, "ny = ", ny)
        else:
            dx, dy = -dy, dx
            print("dx = ", dx, "dy = ", dy)
            x, y = x + dx, y + dy
    return array


def print_spiral(array):
    n = range(len(array))
    for y in n:
        for x in n:
            print(array[x][y], end=' ')
        print()


n = int(input())
print_spiral(spiral(n))
