def gift_inschrijven(klas_bedrag, alle_giften):
    if klas_bedrag[0] not in alle_giften:
        alle_giften[klas_bedrag[0]] = klas_bedrag[1]
    else:
        alle_giften[klas_bedrag[0]] += klas_bedrag[1]

    return alle_giften

