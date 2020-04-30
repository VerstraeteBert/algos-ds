def verlaat_ploeg(deelnemer, ploeg, dictionary):
    dictionary[ploeg].remove(deelnemer)
    if len(dictionary[ploeg]) == 0:
        del dictionary[ploeg]
    return dictionary
    
def vervoegt_ploeg(deelnemer, ploeg, dictionary):
    if ploeg in dictionary and deelnemer not in dictionary[ploeg]:
        dictionary[ploeg].append(deelnemer)
    else:
        dictionary[ploeg] = [deelnemer]
    return dictionary
        