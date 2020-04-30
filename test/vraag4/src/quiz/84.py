def verlaat_ploeg(naam, ploeg, dici):
    if ploeg in dici:
        a = dici[ploeg]
        a.remove(naam)
        if len(a) == 0:
            del dici[ploeg]
    return dici

def vervoegt_ploeg(naam, ploeg, dici):
    if ploeg in dici:
        ploegArray = dici[ploeg]
        f = 0
        for i in range(len(ploegArray)):
            if ploegArray[i] == naam:
                f = 1
        if f == 0:
            ploegArray.append(naam)
    else:
        a = []
        a.append(naam)
        dici[ploeg] = a
    return dici