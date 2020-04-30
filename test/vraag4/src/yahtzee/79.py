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
    z = {}
    for steen in sorted(stenen):
        if not steen in z:
            z[steen] = 1
        else:
            z[steen] += 1
    return z


def max_gelijk(stenen):
    h = histogram(stenen)
    return max(h.values())


def is_FullHouse(stenen):
    h = histogram(stenen)
    n = sorted(h.values(), reverse=True)
    return n[0] == 3 and n[1] == 2


def grootste_score(stenen):
    z = 0
    if is_Yathzee(stenen):
        z = 50
    elif is_grote_straat(stenen):
        z = 40
    elif is_kleine_straat(stenen):
        z = 30
    elif is_FullHouse(stenen):
        z = 25
    som = sum(stenen)
    if som > z:
        z = som
    return z
