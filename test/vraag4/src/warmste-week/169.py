#Warmste week
def gift_inschrijven(sponsering, gifts):
    klas, gift = sponsering
    if not klas in gifts:
        gifts[klas] = 0
    gifts[klas] += gift
    return gifts
        