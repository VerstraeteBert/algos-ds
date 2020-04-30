def histogram(stenen):
    histo = {}
    for ogen in stenen:
        if ogen not in histo:
            histo[ogen] = 1
        else:
            histo[ogen] += 1
    return histo

def max_gelijk(stenen):
    histo = histogram(stenen)
    max = 0
    for aantal in histo.values():
        if aantal > max:
            max = aantal

    return max

def is_FullHouse(stenen):
    histo = histogram(stenen)
    if len(histo) == 2:
        if 5 - list(histo.values())[0] == 2 or 5 - list(histo.values())[0] == 3:
            return True
        else:
            return False
    else:
        return False

def is_DrieGelijke(stenen):
    histo = histogram(stenen)
    if 3 in list(histo.values()):
        return True
    else:
        return False

def is_VierGelijke(stenen):
    histo = histogram(stenen)
    if 4 in list(histo.values()):
        return True
    else:
        return False

def is_GroteStraat(stenen):
    stenen.sort()
    for i in range(0, len(stenen)-1):
        if stenen[i+1] != stenen[i] + 1:
            return False
    else:
        return True

def is_KleineStraat(stenen):
    for u in range(0, len(stenen)):
        controle = stenen[:]
        controle.pop(u)
        if is_GroteStraat(controle):
            return True
    else:
        return False

def is_Kans(stenen):
    histo = histogram(stenen)
    if 2 in list(histo.values()):
        return True
    else:
        return False

def is_Yahtzee(stenen):
    histo = histogram(stenen)
    if len(histo) == 1:
        return True
    else:
        return False

def grootste_score(stenen):
    scores = list()
    if is_DrieGelijke(stenen):
        scores.append(sum(stenen))
    if is_VierGelijke(stenen):
        scores.append(sum(stenen))
    if is_KleineStraat(stenen):
        scores.append(30)
    if is_GroteStraat(stenen):
        scores.append(40)
    if is_FullHouse(stenen):
        scores.append(25)
    if is_Kans(stenen):
        scores.append(sum(stenen))
    if is_Yahtzee(stenen):
        scores.append(50)
    if scores == []:
        scores.append(sum(stenen))

    return max(scores)