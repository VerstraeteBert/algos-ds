def verlaat_ploeg(n,p,wb):
    wb[p].remove(n)
    if len(wb[p])==0:
        del wb[p]
    return wb

def vervoegt_ploeg(n,p,wb):
    if p in wb:
        wb[p].append(n)
    else:
        wb[p]=[n]
    return wb