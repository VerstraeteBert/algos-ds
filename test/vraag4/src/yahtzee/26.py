def histogram(stenen):
    geworpen = {}
    for i in sorted(stenen):
        if i in geworpen:
            geworpen[i] += 1
        else:
            geworpen[i] = 1
    return geworpen
