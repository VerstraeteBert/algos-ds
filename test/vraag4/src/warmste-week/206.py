def gift_inschrijven(sponsor,giften):
    klas,bedrag = sponsor
    if klas in giften:
        giften[klas] = giften[klas] + bedrag
    else:
        giften[klas] = bedrag
    return giften