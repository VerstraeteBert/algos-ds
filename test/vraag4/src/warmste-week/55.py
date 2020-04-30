def gift_inschrijven(verdiend, voorlopig):
    if verdiend[0] in voorlopig:
        voorlopig[verdiend[0]] += verdiend[1]
    else:
        voorlopig[verdiend[0]] = verdiend[1]
    return voorlopig