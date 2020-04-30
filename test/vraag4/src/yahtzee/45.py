def histogram(dobbelstenen):
    h = {}
    for ogen in range(min(dobbelstenen), max(dobbelstenen) + 1):
        aantal = dobbelstenen.count(ogen)
        if aantal > 0:
            h[ogen] = aantal
    return h

def max_gelijk(dobbelstenen):
    h = histogram(dobbelstenen)
    return max(h.values())

def is_FullHouse(dobbelstenen):
    h = histogram(dobbelstenen)
    values = []
    for value in h.values():
        values.append(value)
    try:
        return ((values[0] == 2 and values[1] == 3) or (values[1] == 2 and values[0] == 3))
    except IndexError:
        return False

def is_kleineStraat(dobbelstenen):
    h = histogram(dobbelstenen)
    for ogen in h.keys():
        if ogen + 1 in h.keys() and ogen + 2 in h.keys() and ogen + 3 in h.keys():
            return True
    return False

def is_groteStraat(dobbelstenen):
    h = histogram(dobbelstenen)
    for ogen in h.keys():
        if ogen + 1 in h.keys() and ogen + 2 in h.keys() and ogen + 3 in h.keys() and ogen + 4 in h.keys():
            return True
    return False

def is_yathzee(dobbelstenen):
    h = histogram(dobbelstenen)
    return len(h.keys()) == 1

def grootste_score(dobbelstenen):
    h = histogram(dobbelstenen)
    scores = []
    
    score = 0
    for ogen, aantal in h.items():
        score += ogen * aantal
    scores.append(score)
    
    if is_yathzee(dobbelstenen):
        scores.append(50)
    if is_FullHouse(dobbelstenen):
        scores.append(25)
    if is_groteStraat(dobbelstenen):
        scores.append(40)
    if is_kleineStraat(dobbelstenen):
        scores.append(30)
    
    return max(scores)