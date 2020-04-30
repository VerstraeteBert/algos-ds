def synoniemen(tekst, woordenboek):
    zin = []
    for i in tekst.split():
        if i in woordenboek:
            zin.append(woordenboek[i])
        else:
            zin.append(i)
    return ' '.join(zin)
