def histogram(stenen):

    hist = {}

    for steen in sorted(stenen):

        if not steen in hist:

            hist[steen] = 1

        else:

            hist[steen] += 1

    return hist

def max_gelijk(stenen):

    lijst = histogram(stenen)

    max = 0

    for steen in lijst:

        if lijst[steen] > max:

            max = lijst[steen]

    return max

def is_FullHouse(stenen):
    
    hist = histogram(stenen)
    
    aantallen = sorted(hist.values(), reverse=True)
    
    if aantallen[0] == 3 and aantallen[1] == 2:
        
        return True
    
    else:
        
        return False


