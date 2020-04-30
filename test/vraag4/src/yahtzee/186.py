def som(stenen):
    som = 0
    for getal in stenen:
        som += int(getal)
    return som


def is_Yathzee(stenen):
    for i in range(len(stenen) - 1):
        if not stenen[i] == stenen[i + 1]:
            return False
    return True


def is_grote_straat(stenen):
    stenen.sort()
    for i in range(len(stenen) - 1):
        if not int(stenen[i]) + 1 == int(stenen[i + 1]):
            return False
    return True

def is_kleine_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    tel = 1
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] == gesorteerde_stenen[i - 1] + 1:
            tel += 1
        else:
            if tel >= len(gesorteerde_stenen) - 1:
                return True
            if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1]:
                tel = 1  # herbegin telling

    return tel >= len(stenen) - 1

def histogram(stenen):
    dictionnary = {}
    stenen.sort()
    vorig_getal = 'x'
    for getal in stenen:

        if vorig_getal != getal:
            dictionnary[getal] = 0
        vorig_getal = getal
    for getal in stenen:
        dictionnary[getal] += 1
    return dictionnary

def max_gelijk(stenen):
    dictionnary = histogram(stenen)
    hoogste = 0
    for cijfer in dictionnary:
        if dictionnary[cijfer] > hoogste:
            hoogste = dictionnary[cijfer]
    return hoogste

def is_FullHouse(stenen):
    dictionnary = histogram(stenen)
    for cijfer in dictionnary:
        if not dictionnary[cijfer] in (2,3):
            return False
    return True

def grootste_score(stenen):
    getal1 = som(stenen)
    getal2 = 0
    if is_Yathzee(stenen):
        return 50

    elif is_grote_straat(stenen):
        return 40
    elif is_kleine_straat(stenen):
        return 30
    elif is_FullHouse(stenen):
        getal2 = 25
    lijst = [getal1, getal2]
    maximum = max(lijst)
    return maximum
    