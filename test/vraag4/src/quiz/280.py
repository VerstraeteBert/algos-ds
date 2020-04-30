def verlaat_ploeg(naam, ploeg, dicte):
    dictionnary = dicte
    lijst = dictionnary[ploeg]
    namen = []
    for woord in lijst:
        if woord != naam:
            namen.append(woord)
    dictionnary[ploeg] = namen
    if not namen:
        del dictionnary[ploeg]
    return dictionnary

def vervoegt_ploeg(naam, ploeg, dictionnary):
    if ploeg in dictionnary:
        dictionnary[ploeg].append(naam)
    else:
        dictionnary[ploeg] = [naam]
    return dictionnary