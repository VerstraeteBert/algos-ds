def gift_inschrijven(giften, woordenboek):
    klas, gift = giften
    if klas not in woordenboek:
        woordenboek[klas] = 0
    woordenboek[klas] += gift
    return woordenboek