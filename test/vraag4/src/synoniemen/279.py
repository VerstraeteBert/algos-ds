def synoniemen(tekst, synoniemen):
    res = []
    lijst_tekst = tekst.split()
    for item in lijst_tekst:
        if item in synoniemen.keys():
            res.append(synoniemen[item])
        else:
            res.append(item)
    return " ".join(res)
