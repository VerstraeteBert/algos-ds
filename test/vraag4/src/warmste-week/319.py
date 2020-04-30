def gift_inschrijven(schenking, wboek):
    klas, bedrag=schenking[:]
    if klas in wboek.keys():
        wboek[klas]+=bedrag
    else:
        wboek[klas]=bedrag
    return wboek