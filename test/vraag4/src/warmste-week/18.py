def gift_inschrijven(klas, woordenboek):
    if klas[0] in woordenboek:
        woordenboek[klas[0]] += klas[1]
    else:
        woordenboek[klas[0]] = klas[1]
    return woordenboek
        