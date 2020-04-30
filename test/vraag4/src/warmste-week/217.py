def gift_inschrijven(klas_bedrag, woordenboek):
    klas = klas_bedrag[0]
    bedrag = klas_bedrag[1]
    if klas in woordenboek:
        woordenboek[klas] += bedrag
    else:
        woordenboek[klas] = bedrag
    return woordenboek    