def verlaat_ploeg(naam,ploeg,dict):
    lege_ploeg = ''
    for pl in dict:
        if pl == ploeg:
            dict[pl].remove(naam)
            if len(dict[pl])==0:
                lege_ploeg = pl
    if lege_ploeg != '':
        del dict[lege_ploeg]
    return dict

def vervoegt_ploeg(naam,ploeg,dict):
    found = 0
    for pl in dict:
        if pl == ploeg:
            dict[pl].append(naam)
            found = 1
    if found == 0:
        dict[ploeg] = [naam]
    return dict
