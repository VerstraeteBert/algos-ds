def verlaat_ploeg(naam, ploeg, boek):
    if len(boek[ploeg]) > 1:
        boek[ploeg].remove(naam)
    else:
        del boek[ploeg]
    return boek

def vervoegt_ploeg(naam, ploeg, boek):
    if ploeg in boek.keys():
        boek[ploeg].append(naam)
    else:
        boek[ploeg] = [naam]
    return boek