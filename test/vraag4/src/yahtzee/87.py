def histogram(stenen):
    maximum = max(stenen)
    teller = 0
    aantal = {}
    for i in range(1, maximum + 1):
        if i in stenen:
            teller += stenen.count(i)
            aantal[i] = teller
            teller = 0
    return aantal


def max_gelijk(stenen):
    maximum = max(stenen)
    gelijk = 0
    for i in range(1, maximum + 1):
        teller = 0
        if i in stenen:
            teller += stenen.count(i)
        if teller > gelijk:
            gelijk = teller
    return gelijk


def is_FullHouse(stenen):
    maximum = max(stenen)
    drie = False
    twee = False
    for i in range(1, maximum + 1):
        teller = 0
        if i in stenen:
            teller += stenen.count(i)
        if teller == 3:
            drie = True
        if teller == 2:
            twee = True
    return drie and twee


def is_kleine_straat(stenen):
    kleine_straat = False
    stenen.sort()
    opeenvolgend = 0
    for i in range(len(stenen) - 1):
        if stenen[i] == stenen[i + 1] - 1:
            opeenvolgend += 1
            if opeenvolgend == (len(stenen) - 2):
                kleine_straat = True
        elif stenen[i] == stenen[i + 1]:
            opeenvolgend = opeenvolgend
        else:
            opeenvolgend = 0
    if is_grote_straat(stenen):
        kleine_straat = True
    return kleine_straat


def is_grote_straat(stenen):
    stenen.sort()
    opeenvolgend = 0
    for i in range(len(stenen) - 1):
        if stenen[i] == stenen[i + 1] - 1:
            opeenvolgend += 1
    return opeenvolgend == (len(stenen) - 1)


def grootste_score(stenen):
    som = sum(stenen)
    if is_FullHouse(stenen):
        if som > 25:
            return som
        else:
            return 25
    if max_gelijk(stenen) == 3:
        return som
    if max_gelijk(stenen) == 4:
        return som
    if is_grote_straat(stenen):
        return 40
    if is_kleine_straat(stenen):
        return 30
    if max_gelijk(stenen) == 5:
        return 50
    else:
        return som