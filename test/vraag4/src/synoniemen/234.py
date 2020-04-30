def synoniemen(tekst, lijst):
    tekst = tekst.split(" ")
    nzin = ""
    for woord in tekst:
        if woord in lijst:
            synoniem_woord = lijst[woord]
            nzin += synoniem_woord + " "
        else:
            nzin += woord + " "
    nzin = nzin.strip()
    
    return nzin
