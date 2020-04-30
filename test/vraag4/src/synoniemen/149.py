def synoniemen(tekst,boek):
    r = ""
    p = tekst.split(" ")
    for i in p:
        if i in boek.keys():
            r += boek[i] + " "
        else:
            r += i + " "
    return r[:-1]