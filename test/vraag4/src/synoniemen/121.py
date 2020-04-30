def synoniemen(tekst,synoniem):
    antwoord = ""
    woorden = tekst.split()
    for woord in woorden:
        if woord in synoniem:
            antwoord += synoniem[woord] + " "
        if woord not in synoniem:
            antwoord += woord + " "
    antwoord = antwoord.strip(" ")
    return antwoord