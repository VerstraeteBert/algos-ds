def verlaat_ploeg(naam, ploeg, ploegen):
    namen = ploegen[ploeg]
    namen.remove(naam)
    ploegen[ploeg] = namen
    if ploegen[ploeg] == []:
        ploegen.pop(ploeg)
    return ploegen

def vervoegt_ploeg(naam, ploeg, ploegen):
    if ploeg in ploegen:
        namen = ploegen[ploeg]
        namen.append(naam)
        ploegen[ploeg] = namen
    else:
        ploegen[ploeg] = [naam]
    return ploegen