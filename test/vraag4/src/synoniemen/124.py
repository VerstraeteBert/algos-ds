def synoniemen(zin, woordenboek):
    zins = zin.split()
    for element in zins:
        if element in woordenboek:
            zins.insert(zins.index(element), woordenboek.get(element))
            zins.remove(element)
    return " ".join(zins).strip()