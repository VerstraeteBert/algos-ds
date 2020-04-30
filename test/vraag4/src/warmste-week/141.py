def gift_inschrijven(tup, dictio):
    bedrag = tup[1]
    klas = tup[0]
    if klas in dictio:
        bedrag += dictio[klas]
        dictio[klas] = bedrag
    else:
        dictio[klas] = bedrag
    return dictio