def gift_inschrijven(tup,woordenboek):
    klas=tup[0]
    bedrag=tup[1]
    if klas in woordenboek:
        geld=woordenboek[klas]
        geld+=bedrag
        woordenboek[klas]=geld
    else:
        woordenboek[klas]=bedrag
    return woordenboek