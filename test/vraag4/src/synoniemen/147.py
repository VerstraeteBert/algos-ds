def synoniemen(string, dictio):
    lijst = string.split(" ")
    lijst_syno = []
    for word in lijst:
        if word in dictio:
            lijst_syno.append(dictio[word])
        else:
            lijst_syno.append(word)
    return " ".join(lijst_syno)