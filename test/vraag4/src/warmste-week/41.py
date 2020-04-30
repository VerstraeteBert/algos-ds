def gift_inschrijven(tuple, dic):
    if tuple[0] in dic.keys():
        dic[str(tuple[0])] += tuple[1]
    else:
        dic[str(tuple[0])] = tuple[1]
    return dic