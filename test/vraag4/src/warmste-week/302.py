def gift_inschrijven(klas_bedrag, woordenboek):
    klas, bedrag =klas_bedrag
    if klas in woordenboek:
        woordenboek[klas] += bedrag
    else:
        woordenboek[klas] = bedrag
    return woordenboek
