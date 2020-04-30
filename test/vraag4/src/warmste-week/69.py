def gift_inschrijven(tpl, dict):
    if tpl[0] in dict:
        dict[tpl[0]] += tpl[1]
    else:
        dict[tpl[0]] = tpl[1]
    return dict
        