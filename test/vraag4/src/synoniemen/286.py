def synoniemen(tekst, woordenboek):
    tekst = tekst.lower().strip()
    nieuw = ""
    woorden = tekst.split()
    for woord in woorden:
        if woord in woordenboek:
            nieuw += woordenboek[woord] + " "
        else:
            nieuw += woord + " "
    return nieuw.strip()