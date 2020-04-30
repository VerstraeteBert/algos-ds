def gift_inschrijven(toevoegen, verzameling):
    klas = toevoegen[0]
    nieuwe_waarde = toevoegen[1]

    if klas in verzameling:
        oude_waarde = verzameling[klas]
        som = oude_waarde + nieuwe_waarde
        verzameling[klas] = som

    else:
        verzameling[klas] = nieuwe_waarde

    return verzameling