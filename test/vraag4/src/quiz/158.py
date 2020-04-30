def verlaat_ploeg(naam, ploeg, dictionary):
    dictionary[ploeg].remove(naam)
    if not dictionary[ploeg]:
        del dictionary[ploeg]
    return dictionary
    
def vervoegt_ploeg(naam, ploeg, dictionary):
    if not ploeg in dictionary:
        dictionary[ploeg] = []
    if not naam in dictionary[ploeg]:
        dictionary[ploeg].append(naam)
    return dictionary