def gift_inschrijven(tup, woordenboek):
    klas , geld = tup
    if klas in woordenboek:
        woordenboek[klas] += geld
    else:
        woordenboek[klas] = geld
    return woordenboek 