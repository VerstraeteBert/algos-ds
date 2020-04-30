def synoniemen(tekst, woordenboek):
    lijst = tekst.split(" ")
    index = 0
    l = len(lijst)
    
    for index in range(l):
        if lijst[index] in woordenboek:
            lijst[index] = woordenboek[lijst[index]]
        index += 1
    resultaat = (" ".join(lijst)).strip()
    return(resultaat)