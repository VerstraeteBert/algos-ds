def gift_inschrijven(klasbedrag, logboek):
    klas, bedrag = klasbedrag
    if klas in logboek:
        logboek[klas] += bedrag
    else:
        logboek[klas] = bedrag
    return logboek