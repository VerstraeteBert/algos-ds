def synoniemen(zin, woordenboek):

    nieuwe_zin = []
    
    for woord in zin.split():

        if woord in woordenboek:

            nieuwe_zin.append(woordenboek[woord])
            
        else:
            
            nieuwe_zin.append(woord)

    return " ".join(nieuwe_zin)




