def gift_inschrijven(sponsoring, overzicht_giften):
    klas = sponsoring[0]
    gift = sponsoring[1]
    if klas in overzicht_giften:
        overzicht_giften[klas] += gift
    else:
        overzicht_giften[klas] = gift
    return overzicht_giften
