def synoniemen(tekst, dict):
    tekst = tekst.split()
    for i in range(len(tekst)):
        if tekst[i] in dict:
            tekst[i] = dict[tekst[i]]
    return " ".join(tekst)
    