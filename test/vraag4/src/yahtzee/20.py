def histogram(s):
    d = {}
    for l in s:
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1
    return d

def max_gelijk(s):
    d = histogram(s)
    m = max(d.values())
    return m

def is_FullHouse(s):
    d = histogram(s)
    if 3 in d.values() and 2 in d.values():
        return True
    return False