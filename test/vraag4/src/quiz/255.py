def verlaat_ploeg(naam, ploeg, dictionary):
    lijst = dictionary[ploeg]
    for el in lijst:
        if el == naam:
            lijst.remove(naam)
            break
    if len(lijst) == 0:
        del dictionary[ploeg]
    else:
        dictionary[ploeg] = lijst
    return dictionary


def vervoegt_ploeg(naam, ploeg, dictionary):
    if ploeg in dictionary:
        lijst = dictionary[ploeg]
        lijst.append(naam)
        dictionary[ploeg] = lijst
    else:
        list = []
        list.append(naam)
        dictionary[ploeg] = list
    return dictionary