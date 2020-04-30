def gift_inschrijven(klassen, dict):
    if klassen[0] in dict:
        dict[klassen[0]] += klassen[1]
    else:
        dict[klassen[0]] = klassen[1]
    return dict
        