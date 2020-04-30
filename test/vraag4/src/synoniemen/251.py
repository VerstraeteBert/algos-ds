def synoniemen(zin, woordenboek):
    woorden_zin_lijst = zin.split()
    nieuwe_woorden_zin_lijst = []
    for woord in woorden_zin_lijst:
        if woord in woordenboek:
            nieuwe_woorden_zin_lijst.append(woordenboek[woord])
            nieuwe_woorden_zin_lijst.append(' ')
        else:
            nieuwe_woorden_zin_lijst.append(woord)
            nieuwe_woorden_zin_lijst.append(' ')
    nieuwe_zin = ''.join(str(e) for e in nieuwe_woorden_zin_lijst).strip()
    return nieuwe_zin

