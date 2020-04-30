def verlaat_ploeg(verlater,ploeg,dict):
    dict[ploeg].remove(verlater)
    if not dict[ploeg]:
        del dict[ploeg]
    return dict
def vervoegt_ploeg(vervoeger,ploeg,dict):
    if not ploeg in dict:
        
        dict[ploeg] = [vervoeger]
    else:
        
        dict[ploeg].append(vervoeger)
        
        
    return dict