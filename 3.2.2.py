def get_dict(_string):
    return set(_string.lower().split())


def update_dictionary(_dict, _string):
    for word in get_dict(_string.lower()):
        _dict[word] = _string.lower().split().count(word)
    return _dict


def main():
    _dict = {}
    for item in sorted(update_dictionary(_dict, input())):
        print(item, _dict[item], end=" " '\n')


if __name__ == "__main__":
    main()

