# Warmste week

def gift_inschrijven(t, dict):
    if t[0] in dict:
        dict[t[0]] += t[1]
    else:
        dict[t[0]] = t[1]
    return dict