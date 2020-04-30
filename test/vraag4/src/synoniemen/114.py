def synoniemen(tekst,woordenboek):
    nieuwe_tekst = ""
    tekst_lijst = tekst.split()
    for woord in tekst_lijst:
        if woord in woordenboek:
            nieuwe_tekst += woordenboek[woord] + " "
        else:
            nieuwe_tekst += woord + " "
    return nieuwe_tekst.strip()