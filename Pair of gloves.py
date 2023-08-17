def number_of_pairs(gloves):
    color_count = {}
    for glove in gloves:
        color_count[glove] = color_count.get(glove, 0) + 1

    pairs = 0
    for count in color_count.values():
        pairs += count // 2

    return pairs