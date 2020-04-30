def verlaat_ploeg(n, p, di):
    di[p].remove(n)
    if len(di[p]) == 0:
        di.pop(p)
    return di

def vervoegt_ploeg(n, p, di):
    if p in di:
        di[p].append(n)
    else:
        di[p] = [n]
    return di