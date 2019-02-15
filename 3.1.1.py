def my_func(x):
    if x <= - 2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return - x / 2
    else:
        return (x - 2) ** 2 + 1


def main():
    print(my_func(float(input())))


if __name__ == "__main__":
    main()
