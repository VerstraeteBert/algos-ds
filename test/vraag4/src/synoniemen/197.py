def synoniemen(s, d):
    l = s.split()
    for e in d:
        if e in l:
            for i in range(l.count(e)):
                l.insert(l.index(e), d[e])
                l.remove(e)
    r = ''
    for u in l:
        r += u + ' '

    return r.strip()