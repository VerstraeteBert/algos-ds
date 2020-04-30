def histogram(stenen):
    woordenboek = {}
    sorted_stenen = sorted(stenen)
    for steen in sorted_stenen:
        if steen not in woordenboek:
            woordenboek[steen] = 1
        else:
            woordenboek[steen] += 1
    return woordenboek

def max_gelijk(stenen):
    hist = histogram(stenen)
    return max(hist.values())

def is_FullHouse(stenen):
    hist = histogram(stenen)
    aantallen = sorted(hist.values())
    return aantallen[0] == 2 and aantallen[1] == 3
