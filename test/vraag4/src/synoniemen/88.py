def synoniemen(tekst, woordenboek):
    list=[]
    for element in tekst.split(" "):
        if element in woordenboek:
            list.append(woordenboek[element])
        else:
            list.append(element)
    return (" ").join(list)