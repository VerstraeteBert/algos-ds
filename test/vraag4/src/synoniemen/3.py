def synoniemen(zin, woordenboek):
    lege_string = ""
    
    woorden_lijst = zin.split()
    
    for i in range(0, len(woorden_lijst)):
        if woorden_lijst[i] in woordenboek:
            lege_string += woordenboek[woorden_lijst[i]] + " "
        else:
            lege_string += woorden_lijst[i] + " "
            
    return lege_string.strip()