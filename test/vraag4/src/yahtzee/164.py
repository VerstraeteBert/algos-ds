def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    res = True
    eerste = stenen[0]
    for item in stenen:
        if item != eerste:
            res = False
    return res


def is_grote_straat(stenen):
    stenen.sort()   #ogen van klein naar groot
    res = True
    for i in range(1, len(stenen)):
        if not stenen[i] - 1 == stenen[i-1]:
            res = False
    return res


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
    histogram = {}
    for item in sorted(stenen):
        if item not in histogram:
            histogram[item] = 1
        else:
            histogram[item] += 1
    return histogram


def max_gelijk(stenen):
    aantallen = (histogram(stenen)).values()
    return max(aantallen)


def min_gelijk(stenen):
    aantallen = (histogram(stenen)).values()
    return min(aantallen)


def is_FullHouse(stenen):
        return max_gelijk(stenen) == 3 and min_gelijk(stenen) == 2


def grootste_score(stenen):
    scores = []
    if max_gelijk(stenen) == 3 or max_gelijk(stenen) == 4:
        scores.append(sum(stenen))
    if is_kleine_straat(stenen):
        scores.append(30)
    if is_grote_straat(stenen):
        scores.append(40)
    if is_FullHouse(stenen):
        scores.append(25)
    if is_Yathzee(stenen):
        scores.append(50)
    else:
        scores.append(sum(stenen))
    return max(scores)
