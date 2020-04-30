def synoniemen(tekst,wb):
    woorden = tekst.split(" ")
    for i in range (len(woorden)):
        synoniem = wb.get(woorden[i])
        if synoniem != None:
            woorden[i]=synoniem
    zin =""
    for woord in woorden:
        zin += woord
        zin += " "
    zin = zin[:-1]
    return zin
        