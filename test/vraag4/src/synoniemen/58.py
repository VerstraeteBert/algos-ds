def synoniemen(tekst, synoniemenwoordenboek):
    aangepastetekst = ""
    tekst1 = tekst.strip()
    tekst2 = tekst1.split(" ")
    for i in tekst2:
        if i in synoniemenwoordenboek:
            aangepastetekst += synoniemenwoordenboek[i] + " "
        else:
            aangepastetekst += i + " "
    return aangepastetekst.strip()