def synoniemen(zin, woordenboek):
    lijst = zin.split()
    nieuw = []
    for i in lijst:
        if i in woordenboek.keys():
            nieuw.append(woordenboek[i])
        else:
            nieuw.append(i)
    return " ".join(nieuw)