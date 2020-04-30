import string
def synoniemen(tekst, woordenboek):
    vervangen =[]
    tekst1 = tekst.split()
    for woord in tekst1:
        if woord in woordenboek:
            vervangen.append(woordenboek[woord])
        else:
            vervangen.append(woord)
    resultaat = " ".join(vervangen)
    return resultaat