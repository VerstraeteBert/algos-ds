
def gift_inschrijven(tuple, dictionary):
    try:
        dictionary[tuple[0]] += tuple[1]
    except KeyError:
        dictionary[tuple[0]] = tuple[1]
    return dictionary