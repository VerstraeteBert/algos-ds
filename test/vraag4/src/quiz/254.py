def verlaat_ploeg(deelnemer, ploeg, dictionary):
    dictionary[ploeg].remove(deelnemer)
    if not dictionary[ploeg]:
        del dictionary[ploeg]
    return dictionary
def vervoegt_ploeg(deelnemer, ploeg, dictionary):
    if not ploeg in dictionary:
        dictionary[ploeg] = []
    if not deelnemer in dictionary[ploeg]:
        dictionary[ploeg].append(deelnemer)
    return dictionary