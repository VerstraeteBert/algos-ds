def gift_inschrijven(klas, totaal):

    for i in totaal.copy():
        if klas[0] == i:
            totaal[i] += klas [1]
        elif klas[0] not in totaal:
            totaal[klas[0]] = klas[1]

    return totaal