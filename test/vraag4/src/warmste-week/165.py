def gift_inschrijven(klas, dictionary):
    key, value = klas
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += value
    return dictionary