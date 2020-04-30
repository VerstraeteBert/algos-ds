def synoniemen(tekst, woordenboek):
    zin = tekst.split()
    nieuw = []
    for i in range(len(zin)):
        if zin[i] in woordenboek:
            nieuw.append(woordenboek[zin[i]])


        else:
            nieuw.append(zin[i])
    return ' '.join(nieuw)
