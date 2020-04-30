def gift_inschrijven(klas, totaal):


    bedrag = klas[1]
    bedrag = float(bedrag)
    klas = klas[0]
    n = 0

    for k in totaal:
        if k == klas:
            bedrag2 = totaal[k]
            bedrag2 = float(bedrag2)
            bedrag += bedrag2
            totaal[k] = bedrag
            n = 1
            
    if n == 0:
            totaal[klas] = bedrag
        
    return totaal