def synoniemen(tekst, woordenboek):
    tekst_lijst=tekst.split()
    aangepaste_tekst=[]
    for woord in tekst_lijst:
        if woord in woordenboek:
            woord=woordenboek[woord] #woord wordt vervangen door zijn synoniem
        aangepaste_tekst.append(woord)
    return ' '.join(aangepaste_tekst)
        