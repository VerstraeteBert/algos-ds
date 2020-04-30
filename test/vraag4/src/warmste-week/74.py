def gift_inschrijven(don, dic):
    klas, donatie = don
    if klas in dic:
        dic[klas] += donatie
    else:
        dic[klas] = donatie
    return dic