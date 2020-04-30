def synoniemen(tekst, woordenboek):
    uitvoer = ''
    l = tekst.split()
    for woord in l:
        if woord in woordenboek.keys():
            uitvoer += woordenboek.get(woord) + ' '
        else:
            uitvoer += woord + ' '
    return uitvoer[:-1]
            