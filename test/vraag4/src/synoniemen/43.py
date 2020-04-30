def synoniemen(tekst, woordb):
    tekst_n = ""
    lijst = tekst.split()
    for woord in lijst:
        if woord in woordb:
            woord1 = woordb[woord]
            tekst_n += woord1 +" "
        else:
            tekst_n += woord + " "
    return tekst_n[:-1]
            
    