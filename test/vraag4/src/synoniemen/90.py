def synoniemen(tekst, synoniemenboek):
    bla = tekst
    for woord, synoniem in synoniemenboek.items():
        bla.replace(woord, synoniem)
    return bla