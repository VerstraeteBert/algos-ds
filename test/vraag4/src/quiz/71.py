def verlaat_ploeg(naam, ploeg, ploegen):

    ploegen[ploeg].remove(naam)

    if not ploegen[ploeg]:

        del ploegen[ploeg]

    return ploegen

def vervoegt_ploeg (naam, ploeg, ploegen):

    if not ploeg in ploegen:

        ploegen[ploeg] = []

    if not naam in ploegen[ploeg]:

        ploegen[ploeg].append(naam)
        
    return ploegen