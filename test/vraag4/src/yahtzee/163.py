def histogram(stenen):
    lijst = {}
    for steen in sorted(stenen):
        if steen in lijst:
            lijst[steen] += 1
        else:
            lijst[steen] = 1
    return lijst
