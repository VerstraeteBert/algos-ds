def gift_inschrijven(nieuw,verzameling):
    if nieuw[0] in verzameling:
        klas=nieuw[0]
        bedrag=float(verzameling[klas])
        nieuw_bedrag=bedrag+float(nieuw[1])
        verzameling[klas]=nieuw_bedrag
    if nieuw[0] not in verzameling:
        klas = nieuw[0]
        verzameling[klas]=nieuw[1]
    return verzameling