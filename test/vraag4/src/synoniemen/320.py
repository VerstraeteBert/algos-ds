def synoniemen(zin,dic):
    lijst = zin.split(" ")
    zin_nieuw =""
    for el in lijst:
        if el in dic:
            zin_nieuw += dic[el]
        else:
            zin_nieuw += el
        zin_nieuw += " "
    return(zin_nieuw[:-1])
