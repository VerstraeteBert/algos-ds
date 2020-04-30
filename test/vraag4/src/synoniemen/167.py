def synoniemen(zin, woordenboek):

    opl = ""
    for woord in zin.split():
        if woord in woordenboek:
            opl += woordenboek[woord]
            opl += " "
        else:
            opl += woord
            opl += " "

    return opl.strip()
