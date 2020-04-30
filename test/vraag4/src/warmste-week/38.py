def gift_inschrijven(sponsor, geld):
    klas, gift = sponsor

    if not klas in geld:
        geld[klas] = 0

    geld[klas] += gift
    return geld