def synoniemen(tekst,synoniemenwoordenboek):
    nieuwe_tekst = ""
    lijst_van_woorden = tekst.split(" ")
    for woord in lijst_van_woorden:
        if woord in synoniemenwoordenboek:
            nieuwe_tekst += synoniemenwoordenboek[woord] + " "
        else:
            nieuwe_tekst += woord+ " "

    return nieuwe_tekst.strip()