def gift_inschrijven(tuple,dictionary):
    if tuple[0] in dictionary:
        som = tuple[1] + dictionary[tuple[0]]
        dictionary[tuple[0]] = som
    else:
        dictionary[tuple[0]] = tuple[1]

    return dictionary