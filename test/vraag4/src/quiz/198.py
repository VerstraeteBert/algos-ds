def verlaat_ploeg(persoon, ploeg, dictionary):
    lijst = dictionary[ploeg]
    lijst.remove(persoon)
    if len(lijst) == 0:
        del dictionary[ploeg]
    else:
        dictionary[ploeg] = lijst
    return dictionary


def vervoegt_ploeg(persoon, ploeg, dictionary):
    if ploeg not in dictionary:
        dictionary[ploeg] = [persoon]
    else:
        dictionary[ploeg].append(persoon)
    return dictionary

