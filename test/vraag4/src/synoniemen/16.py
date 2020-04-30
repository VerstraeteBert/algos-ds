def synoniemen(zin, woordenboek):
    li = list(zin.split(" "))
    l = []
    for i in li:
        if i in woordenboek:
            l.append(woordenboek[i])
        else:
            l.append(i)
    
    return " ".join(l)