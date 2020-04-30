def gift_inschrijven(bedrag_klas, giften_per_klas):
    if bedrag_klas[0] in giften_per_klas:
        giften_per_klas[bedrag_klas[0]] = bedrag_klas[1] + giften_per_klas[bedrag_klas[0]]
    if bedrag_klas[0] not in giften_per_klas:
        giften_per_klas[bedrag_klas[0]] = bedrag_klas[1]
    return giften_per_klas