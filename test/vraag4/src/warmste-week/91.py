def gift_inschrijven(a, b):
    zoek = (a[0])
    bedrag = (a[1])
    if zoek in b:
        oudbedrag = b[zoek]
        bedrag = round(bedrag + oudbedrag, 2)
        b[zoek] = bedrag       
    else:
        b[zoek] = bedrag
    return b
