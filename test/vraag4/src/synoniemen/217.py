def synoniemen(zin, woordenboek):
    lijst = zin.split()
    lijst2 = []
    for woord in lijst:
        if woord in woordenboek.keys():
            lijst2.append(woordenboek[woord])
        else:
            lijst2.append(woord)
    aangepaste_zin = ' '.join(lijst2)
    return aangepaste_zin
