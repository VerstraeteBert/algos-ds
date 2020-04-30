def synoniemen(zin, woordenboek):
    zin = zin.split()
    x = 0
    for i in zin:
        if i in woordenboek:
            zin[x] = woordenboek[i]
        x += 1
    zin = ' '.join(zin)
    return zin