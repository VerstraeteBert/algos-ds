def histogram(ogen):
    hist = {}
    for i in sorted(ogen):
        if not i in hist:
            hist[i] = 1
        else:
            hist[i] += 1
    return hist
    
def max_gelijk(ogen):
    max = 0
    for i in ogen:
        aantal = ogen.count(i)
        if aantal > max:
            max = aantal
    return max
            
def is_FullHouse(ogen):
    k = 0
    l = 0
    for p in ogen:
        aantal = ogen.count(p)
        if aantal == 3:
            k = 1
        if aantal == 2:
            l = 1
    if k == 1 and l == 1:
        return True
    else: return False