def verlaat_ploeg(naam, naam_ploeg, dictionary):
    dictionary[naam_ploeg].remove(naam)
    if not dictionary[naam_ploeg]:
        del dictionary[naam_ploeg]
    return dictionary


def vervoegt_ploeg(naam, naam_ploeg, dictionary):
    if not naam_ploeg in dictionary:
        dictionary[naam_ploeg] = []
    if not naam in dictionary[naam_ploeg]:
        dictionary[naam_ploeg].append(naam)
    return dictionary 