def gift_inschrijven(Tuple, woordenboek):
    klas=Tuple[0]
    if klas in woordenboek:
        woordenboek[klas] += Tuple[1]
    else:
        woordenboek[klas] = Tuple[1]
    return woordenboek