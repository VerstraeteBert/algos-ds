
def histogram(stenen):
    dictionary = {}
    for worp in sorted(stenen):
        dictionary[int(worp)] = stenen.count(worp)
    return dictionary

def max_gelijk(stenen):
    return histogram(stenen)[max(stenen, key=stenen.count)]

def is_KleineStraat(stenen):
    worp = list(histogram(stenen).keys())
    if len(worp) == 4:
        return worp in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])
    return "1, 2, 3, 4" in str(sorted(stenen)) or "2, 3, 4, 5" in str(sorted(stenen)) or "3, 4, 5, 6" in str(sorted(stenen))

def is_FullHouse(stenen):
    return sorted(list(histogram(stenen).values())) == [2, 3]

def grootste_score(stenen):
    if list(histogram(stenen).values()) == [5]:
        return 50
    if sorted(stenen) == [1, 2, 3, 4, 5] or sorted(stenen) == [2, 3, 4, 5, 6]:
        return 40
    if is_KleineStraat(stenen):
        return 30
    if is_FullHouse(stenen) and sum(stenen) < 25:
        return 25
    return sum(stenen)