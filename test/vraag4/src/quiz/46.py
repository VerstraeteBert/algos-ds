def verlaat_ploeg(naam,ploeg,ploegen):
    if ploeg in ploegen.keys() and naam in ploegen[ploeg]:
            namen = ploegen[ploeg]
            namen.remove(naam)
    if len(ploegen[ploeg])== 0:
        del ploegen[ploeg]
    return ploegen
def vervoegt_ploeg(naam,ploeg,ploegen):
    if ploeg in ploegen.keys() and naam not in ploegen[ploeg]:
        namen = ploegen[ploeg]
        namen.append(naam)
    else:
        ploegen.update({ploeg:[naam]})
    return ploegen