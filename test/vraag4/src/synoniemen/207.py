def synoniemen(zin, woordenboek):
    lijst1 = zin.split(' ')
    lijst2 = []
    for woord in lijst1:
        if woord in woordenboek:
            lijst2.append(woordenboek[woord])
        else:
            lijst2.append(woord)
    zin2 = ' '.join(lijst2)
    return zin2