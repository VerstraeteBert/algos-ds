def gift_inschrijven(giften, dictionary):
    klas, getal = giften
    if klas not in dictionary:
        dictionary[klas] = 0
    dictionary[klas] += getal
    return dictionary