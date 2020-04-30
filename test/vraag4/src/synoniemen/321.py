def synoniemen(tekst,synoniem):
    tekst = tekst.split()
    for i in range(len(tekst)):
        if tekst[i] in synoniem:
            tekst[i] = synoniem[tekst[i]]
    return ' '.join(tekst)