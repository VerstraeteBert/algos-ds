def gift_inschrijven(klasbedrag, dictionary):
    klas, bedrag = klasbedrag
    if klas in dictionary:
        dictionary[klas] += bedrag
    else:
        dictionary[klas] = bedrag
    return dictionary