def synoniemen(string, dictionary):
    list = string.split()
    for i in range(len(list)):
        try:
            list[i] = dictionary[list[i]]
        except KeyError:
            continue
    return " ".join(list)