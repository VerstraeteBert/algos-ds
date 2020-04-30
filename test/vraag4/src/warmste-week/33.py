def gift_inschrijven(tupel, woordenboek):
    if tupel[0] in woordenboek:
        woordenboek[tupel[0]] += tupel[1]
    else:
        woordenboek[tupel[0]] = tupel[1]
    return woordenboek