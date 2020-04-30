def verlaat_ploeg(naam, ploeg, dicti):
    for key in dicti:
        if key == ploeg:
            l = dicti[key]
            for deelnemer in l:
                if deelnemer == naam:
                    l.remove(l[l.index(naam)])
            dicti[ploeg] = l
    if len(l) == 0:
        del dicti[ploeg]
    return dicti
    
def vervoegt_ploeg(naam, ploeg, dicti):
    i = 0
    for key in dicti:
        if key == ploeg:
            dicti[ploeg].append(naam)
            i = 1
    if i == 0:
        dicti[ploeg] = [naam]
    return dicti
    