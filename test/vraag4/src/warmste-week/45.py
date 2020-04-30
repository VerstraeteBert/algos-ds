def gift_inschrijven(tulp, dict):

    if tulp[0] in dict:
        dict[tulp[0]] = dict.get(tulp[0])+ tulp[1]
    else:
        dict[tulp[0]] = tulp[1]
    return dict