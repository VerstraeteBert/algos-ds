def gift_inschrijven(klasbedrag, teller):
    klas, bedrag = klasbedrag
    if klas in teller:
        teller[klas] += bedrag
    else:
        teller[klas] = bedrag
        
    return teller

    