def histogram(stenen):
    histogram = {}
    for i in stenen:
        if i in histogram:
            histogram[i] += 1
        else:
            histogram[i] = 1
    return histogram


def max_gelijk(stenen):
    grootste = 0
    for i in stenen:
        if histogram(stenen)[i] > grootste:
            grootste = histogram(stenen)[i]
    return grootste


def is_FullHouse(stenen):
    if max_gelijk(stenen) == 3:
        for i in stenen:
            if histogram(stenen)[i] == 2:
                return True
    return False


def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    stenen.sort()
    return stenen[0] == stenen[-1]


def is_grote_straat(stenen):
    stenen.sort()
    for i in range(1, len(stenen)):
        if int(stenen[i]) != int(stenen[i-1]+1):
            return False
    return True


def is_kleine_straat(stenen):
    stenen.sort()
    test = []
    for i in range(1, len(stenen)):
        if int(stenen[i]) != int(stenen[i-1]+1):
            if i-1 == 0 or i == len(stenen)-1:
                continue
            elif int(stenen[i]) == int(stenen[i-1]):
                continue
            else:
                return False
        else:
            test.append(i-1)
    test.append(i)
    # print(test)
    if len(test) < len(stenen)-1:
        return False
    return True


def grootste_score(stenen):
    scores = [0]
    scores.append(som(stenen))
    if is_kleine_straat(stenen):
        scores.append(30)
    if is_grote_straat(stenen):
        scores.append(40)
    if is_FullHouse(stenen):
        scores.append(25)
    if is_Yathzee(stenen):
        scores.append(50)
    eindscore = max(scores)
    return eindscore
