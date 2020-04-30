def gift_inschrijven(klas_bedrag, giften):
    klas=klas_bedrag[0]
    bedrag=klas_bedrag[1]
    if klas in giften:
        begin=giften[klas]
        einde=begin+bedrag
        giften[klas]=einde
    else:
        giften[klas]=bedrag
    return giften