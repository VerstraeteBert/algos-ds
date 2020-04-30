def gift_inschrijven(klasbedrag, woordenboek):
    for klas in woordenboek:
        if klasbedrag[0]== klas:
            woordenboek[klas] += klasbedrag[1]
    if klasbedrag[0] not in woordenboek:
        woordenboek[klasbedrag[0]] = klasbedrag[1]
    return woordenboek