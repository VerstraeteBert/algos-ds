def histogram(stenen):
    over = {}
    for i in stenen:
        if i in over.keys():
            over[i] += 1
        else:
            over[i] = 1
    return over


def max_gelijk(stenen):
    grootste = 0
    for i in histogram(stenen).values():
        if i > grootste:
            grootste = i
    return grootste

def is_FullHouse(stenen):
    x = histogram(stenen)
    return len(x) == 2 and max_gelijk(stenen) == 3


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

def is_grote_straat(stenen):
    vergelijk = list(range(1, len(stenen) + 1))
    vergelijk2 = list(range(2,7))
    stenen.sort()
    return stenen == vergelijk or stenen == vergelijk2

def grootste_score(stenen):
    score = 0
    if max_gelijk(stenen) == 3 or max_gelijk(stenen) == 4:
        punten = sum(stenen)
        if punten > score:
            score = punten
    if is_kleine_straat(stenen):
        punten = 30
        if punten > score:
            score = punten
    if is_grote_straat(stenen):
        if 40 > score:
            score = 40
    if is_FullHouse(stenen):
        if 25 > score:
            score = 25
    if max_gelijk(stenen) == 5:
        score = 50
    else:
        punten = sum(stenen)
        if punten > score:
            score = punten
    return score
