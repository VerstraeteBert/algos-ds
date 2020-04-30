def verlaat_ploeg(naam, ploeg, lijst):
    spelers = lijst[ploeg]
    spelers.remove(naam)
    if spelers:    
        lijst[ploeg] = spelers
    else:
        del lijst[ploeg]
    return lijst
    
def vervoegt_ploeg(naam, ploeg, lijst):
    if ploeg in lijst:
        if not naam in lijst[ploeg]:
            lijst[ploeg].append(naam)
    else:
        lijst[ploeg] = [naam]
    return lijst