def synoniemen(tekst, woordenboek):
    lijst = tekst.split()
    zin = ''
    for i in range(len(lijst)):
        woord = lijst[i]
        if woord in woordenboek:
            lijst[i] = woordenboek[woord]
    for woord in lijst:
        zin += woord + ' '
    zin = zin.strip()
    return zin