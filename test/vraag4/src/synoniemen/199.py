def synoniemen(tekst, synoniem_lijst):
    zin = ""
    tekst = tekst.split(" ")
    for woord in tekst:
        if woord in synoniem_lijst:
            zin += synoniem_lijst[woord] + " "
        else:
            zin += woord + " "
    return zin.strip()
