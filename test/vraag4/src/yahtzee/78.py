def histogram(stenen):
    bibl = {}
    for steen in stenen:
        if steen in bibl:
            bibl[steen] += 1
        else:
            bibl[steen] = 1
    return bibl

def max_gelijk(stenen):
    hoogste = int()
    for aantal in histogram(stenen).values():
        if aantal > hoogste:
            hoogste = aantal
    return hoogste

def is_FullHouse(stenen):
    trio = False
    duo = False
    for aantal in histogram(stenen).values():
        if aantal == 2:
            duo = True
        if aantal == 3:
            trio = True
    if duo and trio == True:
        return True
    else: return False