def synoniemen(zin, dictionary):
    nieuw = ""
    zin = zin.split()
    for woord in zin:
        if woord in dictionary:
            nieuw += dictionary[woord] + " "
        else:
            nieuw += woord + " "
    return nieuw.strip()