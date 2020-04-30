def grootste_score(stenen):
    if is_Yathzee(stenen):
        return 50
    if is_grote_straat(stenen):
        return 40
    if is_kleine_straat(stenen):
        return 30
    #3 gelijke of 4 gelijke of kans: score berekenen
    score = som(stenen)
    if score >= 25:
        return score
    if is_FullHouse(stenen):
        return 25
    return score

