def gift_inschrijven(klas,tot):
    found = 0
    for k in tot:
        if k == klas[0]:
            tot[k] = tot[k] + klas[1]
            found = 1

    if found == 0:
        tot[klas[0]] = klas[1]
    return tot
