def gift_inschrijven(tup_klas_bedrag, giften):
    klas, bedrag = tup_klas_bedrag
    if klas in giften:
        giften[klas] += bedrag
    if klas not in giften:
        giften[klas] = bedrag
    return giften