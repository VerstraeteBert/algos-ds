def gift_inschrijven(sponsoring, woordenboek):
    klas, gift = sponsoring
    if not klas in woordenboek:
        woordenboek[klas] = 0
    woordenboek[klas] += gift
    return woordenboek