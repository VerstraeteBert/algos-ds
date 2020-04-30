def synoniemen(tekst, dictionary):
    list = tekst.split()
    for i in range(len(list)):
        if str(list[i]) in dictionary:
            list[i] = dictionary[str(list[i])]
    resultaat = ' '.join(list)
    return resultaat