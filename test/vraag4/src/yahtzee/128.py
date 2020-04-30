def histogram(stenen):
    dicti = {}
    for getal in stenen:
        if getal in dicti.keys():
            dicti[getal] += 1
        else:
            dicti[getal] = 1
    return dicti

def max_gelijk(stenen):
    dicti = histogram(stenen)
    hoogste = max(dicti.values())
    return hoogste


def is_FullHouse(stenen):
    dicti = histogram(stenen)
    klein = 2
    groot = 3
    if klein in dicti.values() and groot in dicti.values():
        return True
    else:
        return False


def som(stenen):
    som = sum(stenen)
    return som


def is_Yathzee(stenen):
    if min(stenen) == max(stenen):
        return True
    else:
        return False


def is_grote_straat(stenen):
    stenen.sort()
    aantal = 0
    for i in range(1, len(stenen)):
        if stenen[i] == stenen[i - 1] + 1:
            aantal += 1
    if aantal == len(stenen) - 1:
        return True
    else:
        return False


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

def grootste_score(stenen):
    score = 0
    if is_Yathzee(stenen):
        score = 50
    elif is_grote_straat(stenen):
        score = 40
    elif is_kleine_straat(stenen):
        score  = 30
    elif is_FullHouse(stenen):
        score = 25

    if score < sum(stenen):
        return sum(stenen)
    else: 
        return score


