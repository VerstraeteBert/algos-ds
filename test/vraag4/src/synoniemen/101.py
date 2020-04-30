def synoniemen(zin, woordenboek):
    lijst = zin.split()
    for i in lijst:
        if i in woordenboek:
            index = lijst.index(i)
            lijst.remove(i)
            lijst.insert(index, woordenboek[i])
    return " ".join(lijst)