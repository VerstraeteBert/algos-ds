def gift_inschrijven(tuple,dic):
    if tuple[0] in dic:
        dic[tuple[0]] += tuple[-1]
    else:
        dic[tuple[0]] = tuple[-1]
    return(dic)
