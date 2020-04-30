def gift_inschrijven(gift, dictionary):
    key, val = gift[0], gift[1]
    if key in dictionary:
        dictionary[key] += val
    else:
        dictionary[key] = val
    return dictionary