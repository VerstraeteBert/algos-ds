def synoniemen(zin, synoniemen):
    lijst = zin.split()
    index = 0
    for i in lijst:
        if i in synoniemen:
            lijst.remove(i)
            lijst.insert(index,synoniemen[i])
        index += 1
    zin_synoniem = " ".join(lijst)
    return zin_synoniem