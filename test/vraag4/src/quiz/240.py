def verlaat_ploeg(name,ploeg,dict):
    dict[ploeg].remove(name)
    if dict[ploeg] == []:
        dict.pop(ploeg)
    return dict





def vervoegt_ploeg(name, ploeg, dict):
    if not ploeg in dict:
        dict[ploeg] = []
    dict[ploeg].append(name)
    return dict