def gift_inschrijven(t,wb):
    if t[0] in wb:
        if t[1]!=wb[t[0]]:
            wb[t[0]]=wb[t[0]]+t[1]
    else:
        wb[t[0]]=t[1]
    return wb