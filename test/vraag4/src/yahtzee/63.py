def histogram(throw: list):
    histo = {}
    for i in throw:
        if i not in histo:
            histo[i] = 1

        else:
            histo[i] += 1
    return histo

def max_gelijk(throw: list):
    return max(histogram(throw))