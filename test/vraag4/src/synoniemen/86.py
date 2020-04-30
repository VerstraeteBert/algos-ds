def synoniemen(tekst, woordenboek):
    lijst = tekst.split()
    for i in range(0, len(lijst)):
        if lijst[i] in woordenboek:
            lijst[i] = woordenboek[lijst[i]]
    resultaat = " ".join(lijst)
    return resultaat