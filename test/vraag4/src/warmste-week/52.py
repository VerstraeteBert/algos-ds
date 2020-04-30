def gift_inschrijven(klasbedrag,woordenboek):
    if klasbedrag[0] in woordenboek.keys():
        woordenboek[klasbedrag[0]] += klasbedrag[1]
    else:
        klas = klasbedrag[0]
        winst = klasbedrag[1]
        woordenboek.update({klas:winst})
    return woordenboek
    