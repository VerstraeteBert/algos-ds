def vervoegt_ploeg(n, p, d):
    if p in d:
        d[p].append(n)
    else:
        d[p] = [n]
    return d

def verlaat_ploeg(n, p, d):
    d[p].remove(n)
    if not d[p]:
        del d[p]
    return d