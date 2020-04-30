def gift_inschrijven(klastuple, status):
    klas, gift = klastuple
    if klas not in status:
        status[klas] = 0
    status[klas] += gift
    return status