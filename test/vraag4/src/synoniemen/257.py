def synoniemen(tekst, woordenboek):
    tekst_lijst = tekst.split()
    nieuwe_zin = []
    for woord in tekst_lijst:
        if woord in  woordenboek:
            nieuwe_zin.append(woordenboek[woord])
        else:
            nieuwe_zin.append(woord)
    return " ".join(nieuwe_zin)
