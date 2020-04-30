def som(stenen):
    return sum(stenen)


def is_Yathzee(stenen):
    gesorteerde_stenen = sorted(stenen)
    return gesorteerde_stenen[0] == gesorteerde_stenen[-1]


def is_grote_straat(stenen):
    gesorteerde_stenen = sorted(stenen)
    for i in range(1, len(gesorteerde_stenen)):
        if gesorteerde_stenen[i] != gesorteerde_stenen[i - 1] + 1:
            return False
    return True
    

def histogram(stenen):
    hist = {}
    for steen in sorted(stenen):
        if not steen in hist:
            hist[steen] = 1
        else:
            hist[steen] += 1
    return hist