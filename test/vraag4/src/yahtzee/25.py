def histogram(worpen):
    histo = {}
    for stenen in sorted(worpen):
        if not stenen in histo:
            histo[stenen] = 1
        else:
            histo[stenen] += 1
    return histo

def max_gelijk(worpen):
    lijst = []
    histo = histogram(worpen)
    for i in histo.values():
        lijst += [i]
    return max(lijst)

def is_FullHouse(worpen):
    histo = histogram(worpen)
    if len(histo) == 2:
        return True
    else:
        return False
