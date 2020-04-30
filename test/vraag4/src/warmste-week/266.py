def gift_inschrijven(bedrag, woordenboek):
    klas = bedrag[0]
    geld = float(bedrag[1])
    if klas in woordenboek:
        reeds = float(woordenboek[klas])
        totaal = reeds + geld
        woordenboek[klas] = float(totaal)
    else:
        woordenboek[klas] = geld
    return woordenboek
print(gift_inschrijven(('5WWI', 78.33),{'6WWI': 64.87, '6BI': 71.63, '5BI': 26.39, '5WWI': 82.68}))