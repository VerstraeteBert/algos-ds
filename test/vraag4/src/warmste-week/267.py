def gift_inschrijven(tuple, dictionary):
    if tuple[0] in dictionary:
        dictionary[str(tuple[0])] += float(tuple[1])
    else:
        dictionary[tuple[0]] = tuple[1]
    return dictionary
