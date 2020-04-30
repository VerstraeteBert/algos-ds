def synoniemen(zin, synoniemen):
    lijst = zin.split(" ")
    lijst = [(str(synoniemen.get(woord))*(woord in synoniemen) + woord*(woord not in synoniemen)) for woord in lijst]
    zin = ""
    for woord in lijst:
        zin += woord + " "
    return zin.strip()