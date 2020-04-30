def histogram(stenen):
    woordenboek = {}
    for i in range(len(stenen)):
        if stenen[i] in woordenboek:
            woordenboek[stenen[i]] += 1
        else:
            woordenboek[stenen[i]] = 1
    return woordenboek


def max_gelijk(stenen):
    woordenboek = histogram(stenen)
    maxGelijk = 0
    for woord in woordenboek:
        if woordenboek[woord] > maxGelijk:
            maxGelijk = woordenboek[woord]
    return maxGelijk

def is_FullHouse(stenen):
    woordenboek = histogram(stenen)
    voorwaarde = 0
    aantal_2 = 0
    aantal_3 = 0
    for woord in woordenboek:
        if woordenboek[woord] == 2 and aantal_2 != 1:
            voorwaarde += 1
            aantal_2 = 1
        elif woordenboek[woord] == 3 and aantal_3 != 1:
            voorwaarde += 1
            aantal_3 = 1
    if voorwaarde == 2:
        return True
    else:
        return False


def is_grote_straat(stenen):
    stenen.sort()
    opeenvolgend = 0
    for i in range(len(stenen) - 1):
        if stenen[i] == stenen[i + 1] - 1:
            opeenvolgend += 1
    return opeenvolgend == (len(stenen) - 1)

def is_Yathzee(stenen):
    gelijk = 0
    for i in range(len(stenen) - 1):
        if stenen[i] == stenen[i + 1]:
            gelijk += 1
    return gelijk == (len(stenen) - 1)

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

def grootste_score(stenen):
    if is_grote_straat(stenen):
        score = 40
    elif is_kleine_straat(stenen):
        score = 30
    elif is_FullHouse(stenen):
        score = 25
        if sum(stenen) > score:
            score = sum(stenen)
    elif is_Yathzee(stenen):
        score = 50
    else:
        score = sum(stenen)
    return score