
def synoniemen(zin, dictionary):
    s_zin = []
    for woord in zin.split():
        try:
            s_zin.append(dictionary[woord])
        except KeyError:
            s_zin.append(woord)
    return " ".join(s_zin)
