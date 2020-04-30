def synoniemen(tekst, dic):
    woorden = tekst.split(" ")
    for i, woord in enumerate(woorden):
        if woord in dic:
            woorden[i] = dic[woord]
        else:
            pass
    zin = " ".join(woorden)
    
    return zin