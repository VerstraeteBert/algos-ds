def synoniemen(tekst,dic):
    woorden = tekst.split()
    for i in range(len(woorden)):
        if woorden[i] in dic:
            woorden[i] = dic[woorden[i]]
    return " ".join(woorden)