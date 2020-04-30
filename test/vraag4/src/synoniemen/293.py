def synoniemen(zin, lijst):
    result = ""
    for i in zin.split(" "):
        if i in lijst.keys():
            result += lijst[str(i)] + " "
        else:
            result += i + " "
    return result[:-1]