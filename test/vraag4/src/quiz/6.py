def verlaat_ploeg(deelnemer, ploeg, dictionary):
    for team in dictionary:
        if ploeg == team:
            a = dictionary[ploeg]
            a.remove(deelnemer)
    if len(a) > 0:
        dictionary[ploeg] = a
    else:
        del dictionary[ploeg]
    return dictionary
    
def vervoegt_ploeg(deelnemer, ploeg, dictionary):
    if ploeg in dictionary:
        for team in dictionary:
            if ploeg == team:
                a = dictionary[ploeg]
                a.append(deelnemer)
                dictionary[ploeg] = a
        return dictionary
    else:
        lijst = []
        lijst.append(deelnemer)
        dictionary[ploeg] = lijst
        return dictionary