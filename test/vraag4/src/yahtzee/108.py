def som(stenen):
    totaal = sum(stenen)
    return totaal


def is_Yathzee(stenen):
    count = 0
    for i in range(len(stenen) - 1):
        if stenen[i] == stenen[i + 1]:
            count += 1
    return count == len(stenen) - 1


def is_grote_straat(stenen):
    stenen.sort()
    count = 0
    for i in range(len(stenen) - 1):
        if stenen[i] == stenen[i + 1] - 1:
            count += 1
    return count == len(stenen) - 1


# def is_kleine_straat(stenen):
#     stenen.sort()
#     count = 0
#     for i in range(len(stenen) - 1):
#         if stenen[i] == stenen[i + 1] - 1:
#             count += 1
#         elif stenen[i] == stenen[i + 1]:
#             count = count
#         else:
#             count = 0
#     return count >= len(stenen) - 2

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
                tel = 1
    return tel >= len(stenen) - 1


def histogram(stenen):
    histo = {}
    for i in sorted(stenen):
        if not i in histo:
            histo[i] = 1
        else:
            histo[i] += 1
    return histo


def max_gelijk(stenen):
    aantal = histogram(stenen)
    maxi = max(aantal.values())
    return maxi


def is_FullHouse(stenen):
    histo = histogram(stenen)
    aantallen = sorted(histo.values(), reverse=True)
    return aantallen[0] == 3 and aantallen[1] == 2


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
    totaal = sum(stenen)
    if totaal > score:
        score = totaal
    return score
