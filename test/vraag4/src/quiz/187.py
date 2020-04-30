def verlaat_ploeg(deelnemer, ploeg, dictionary):
    try:
        if len(dictionary[ploeg]) <= 1:
            del dictionary[ploeg]
        else:
            dictionary[ploeg].remove(deelnemer)
    except:
        pass
    return dictionary
def vervoegt_ploeg(deelnemer, ploeg, dictionary):
    try:
        if ploeg in dictionary:
            if deelnemer not in dictionary[ploeg]:
                dictionary[ploeg].append(deelnemer)
        else:
            dictionary[ploeg] = [deelnemer]
    except:
        pass
    return dictionary