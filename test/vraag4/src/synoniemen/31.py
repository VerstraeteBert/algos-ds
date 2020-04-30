def synoniemen(tekst, woordenboek):
    zin = tekst.split()
    for i in range(len(zin)):
        if zin[i] in woordenboek:
            zin[i] = woordenboek[zin[i]]
    return " ".join(zin)