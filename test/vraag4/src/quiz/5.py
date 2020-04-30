def verlaat_ploeg(naam, ploeg, dict):
    dict[ploeg].remove(naam)
    if dict[ploeg] == []:
        del dict[ploeg]
    return dict


# print(verlaat_ploeg('Tom','Sinbox',{'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))


def vervoegt_ploeg(naam, ploeg, dict):
    if ploeg in dict:
        dict[ploeg].append(naam)
    else:
        dict[ploeg] = [naam]
    return dict

