def verlaat_ploeg(x, y, z):
    a = z[y]
    a.remove(x)
    z[y] = a
    if a == []:
       del z[y]
    return z

def vervoegt_ploeg(x, y ,z):
    if y not in z:
        z[y] = [x]
    else:
        a = z[y]
        a.append(x)
        z[y] = a
    return z