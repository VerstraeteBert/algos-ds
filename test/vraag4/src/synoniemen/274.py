def synoniemen(zin, woordenboek):
    tekst = zin.split()
    lege = []
    for el in tekst:
        if el in woordenboek:
            lege.append(woordenboek[el])
        else:
            lege.append(el)
    return ' '.join(lege)