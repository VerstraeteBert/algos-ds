def verlaat_ploeg(naam, ploeg, source):
    source[ploeg].remove(naam)
    if source[ploeg] == []:
        source.pop(ploeg)
    return source
    
def vervoegt_ploeg(naam, ploeg, source):
    if ploeg in source.keys():
        source[ploeg].append(naam)
    else:
        source.update({ploeg: [naam]})
    return source