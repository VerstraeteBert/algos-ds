def synoniemen(zin, woordenboek):
    l = zin.split(' ')
    uitvoer = ''
    for i in l:
        if i in woordenboek:
            i = woordenboek[i]
        uitvoer += i + ' '
    return uitvoer.strip()