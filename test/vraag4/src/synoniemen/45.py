def synoniemen(zin,woordenboek):
    lijst=zin.split(" ")
    lengte=len(lijst)
    lege=""
    for i in range(0,lengte,1):
        if lijst[i] in woordenboek:
            nieuwe=woordenboek[lijst[i]]
            lege+=(nieuwe+" ")
        else:
            lege+=(lijst[i]+" ")
    lege=lege.strip()
    return lege