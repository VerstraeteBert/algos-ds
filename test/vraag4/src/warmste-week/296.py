def gift_inschrijven(sponsering, giften):
    klas, gift = sponsering
    if not klas in giften:
        giften[klas] = 0
        
    giften[klas] += gift
    
    return giften