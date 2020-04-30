def synoniemen(zin, dic):
    l = zin.split()
    ld = []
    for i in l:
        if i in dic:
            ld.append(dic[i])
        else:
            ld.append(i)
    s = ""
    for j in ld:
        s += j+" "
    s = s.strip()
    return s