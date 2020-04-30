import string
def synoniemen(tekst, woordenboek):
    tekst = tekst.split()
    zin = ""
    for t in range(len(tekst)):
        woord = tekst[t]
        if woord in woordenboek:
            a = woordenboek[woord]
            woord = woord.replace(woord, a)
        zin += woord + " "
    zin = zin.rstrip()
    return zin