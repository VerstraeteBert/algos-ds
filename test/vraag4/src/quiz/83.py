
def verlaat_ploeg(naam, ploeg, dictionary):
    dictionary[ploeg].remove(naam)
    if not dictionary[ploeg]:
        del dictionary[ploeg]
    return dictionary

def vervoegt_ploeg(naam, ploeg, dictionary):
    try:
        dictionary[ploeg].append(naam)
    except KeyError:
        dictionary[ploeg] = [naam]
    return dictionary