def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    gesorteerde_stenen = sorted(stenen)
    return gesorteerde_stenen[0] == gesorteerde_stenen[-1]


def is_grote_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1] + 1:
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
    effectief_geworpen = {}
    for element in stenen:
        if element in effectief_geworpen:
            effectief_geworpen[element] += 1
        else :
            effectief_geworpen[element] = 1
    return effectief_geworpen


def max_gelijk(stenen):
    effectief_geworpen = histogram(stenen)
    return max(effectief_geworpen.values())


def is_FullHouse(stenen):
    effectief_geworpen = histogram(stenen)
    if len(effectief_geworpen) == 2:
        for val in effectief_geworpen.values():
            if val == 3 or val == 2:
                return True
    return False


def grootste_score(stenen):
    score = 0
    if is_Yathzee(stenen):
        score = 50
    elif is_grote_straat(stenen):
        score = 40
    elif is_kleine_straat(stenen):
        score = 30
    elif is_FullHouse(stenen):
        score = 25

    totaal_ogen = sum(stenen)
    if totaal_ogen > score:
        score = totaal_ogen
    return score