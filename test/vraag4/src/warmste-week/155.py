def gift_inschrijven(toevoeging, dict):
    klas, bedrag = toevoeging
    if klas in dict:
        dict[klas] += bedrag
    else:
        dict[klas] = bedrag

    return dict