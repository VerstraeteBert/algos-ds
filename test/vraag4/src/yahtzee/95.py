def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    if stenen.count(stenen[0]) == len(stenen):
        return True
    else:
        return False


def is_grote_straat(stenen):
    stenen.sort()
    for i in range(1, len(stenen)):
        if stenen[i] != stenen[i-1] + 1:
            return False

    return True


def is_kleine_straat(stenen):
    stenen.sort()
    # n = aantal opeenvolgende stenen
    # begint bij n=1!
    n = 1
    for i in range(1, len(stenen)):
        if stenen[i] == stenen[i-1] + 1:
            n += 1
        elif stenen[i] == stenen[i-1]:
            n += 0
        elif not (i == 1 or i == 4):
            n -= 1

    if n >= len(stenen) - 1:
        return True
    else:
        return False


def histogram(stenen):
    dictionary = {}
    for steen in stenen:
        dictionary[steen] = stenen.count(steen)
    return dictionary


def max_gelijk(stenen):
    return max(histogram(stenen).values())


def is_FullHouse(stenen):
    if len(histogram(stenen)) == 2 and max(histogram(stenen).values()) == 3:
        return True
    else:
        return False


def grootste_score(stenen):
    if is_Yathzee(stenen):
        return 50
    else:
        if is_grote_straat(stenen):
            return 40
        else:
            if is_kleine_straat(stenen):
                return 30
            else:
                if is_FullHouse(stenen):
                    if som(stenen) < 25:
                        return 25
                    else:
                        return som(stenen)
                else:
                    return som(stenen)


