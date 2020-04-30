def histogram(stenen):
    stenen.sort()
    histogram = {}
    for i in stenen:
        histogram[i] = 1
    return histogram