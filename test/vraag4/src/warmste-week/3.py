def gift_inschrijven(gift, woordenboek):
    klas, bedrag = gift
    
    if klas in woordenboek:
        reeds_gegeven_bedrag = float(woordenboek[klas])
        bedrag = float(bedrag)
        totaalsom = reeds_gegeven_bedrag + bedrag
        
        woordenboek[klas] = totaalsom
    else:
        woordenboek[klas] = bedrag
        
    return woordenboek