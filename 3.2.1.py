def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    else:
        if 2 * key in d:
            d[2 * key] += [value]
        else:
            d[2 * key] = [value]

