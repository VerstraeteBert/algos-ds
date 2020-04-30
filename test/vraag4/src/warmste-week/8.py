def gift_inschrijven(tuple,dictionary):
    if tuple[0] in dictionary:
        for klas in dictionary:
            if tuple[0] == klas:
                dictionary[klas] = dictionary[klas] + tuple[1]
    else:
        dictionary[tuple[0]] = tuple[1]
    return dictionary