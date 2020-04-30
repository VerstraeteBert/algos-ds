def synoniemen(zin, d):
    l = zin.split()

    for i in range (len(l)):
        if l[i] in d:
            l[i]= d[l[i]]
    return ' '.join(l)