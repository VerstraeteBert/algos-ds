def synoniemen(tekst, woordenboek):
    nieuwe_tekst = ""
    for woord in tekst.split():
        if woord in woordenboek:
            nieuwe_tekst += woordenboek[woord] + " "
        else:
            nieuwe_tekst += woord + " "
    return nieuwe_tekst.strip()