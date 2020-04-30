def verlaat_ploeg(verlaten, ploeg, dictionary):
    deel = dictionary[ploeg]
    deel.remove(verlaten)
    if len(deel) == 0:
        del dictionary[ploeg]
    for woord in dictionary:
        if woord == ploeg:
            dictionary[ploeg] = deel
    return dictionary

def vervoegt_ploeg(vervoegen, ploeg, dictionary):
    if ploeg not in dictionary:
        dictionary[ploeg] = [vervoegen]
    else:
        deel = dictionary[ploeg]
        deel.append(vervoegen)
        for woord in dictionary:
            if woord == ploeg:
                dictionary[ploeg] = deel
    return dictionary