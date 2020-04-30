def synoniemen(zin, d):
    s = ""
    zin = zin.split(" ")
    for i in zin:
        if i in d:
            s += d[i]+" "
        else:
            s += i+" "
    s = s.strip()
    return s