def histogram(stenen):
    a = {}
    for i in range(len(stenen)):
        b = sorted(stenen)
        if b[i] not in a:
            a[b[i]] = 1
        else:
            a[b[i]] += 1
    return a