def gift_inschrijven(gift, dic):
    key=gift[0]
    if key in dic:
        waarde=dic[key]
        waarde2=waarde+ gift[1]
        dic[key]=waarde2
    if key not in dic:
        dic[key]=gift[1]
    return dic