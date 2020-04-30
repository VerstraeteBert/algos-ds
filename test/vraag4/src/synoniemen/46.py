def synoniemen(zin,dict):
    list = zin.split()
    NewList = []

    for i in range(0, len(list)):
        if list[i] in dict:
            NewList.append(dict.get(list[i]))
        else:
            NewList.append(list[i])
    return ' '.join(NewList)