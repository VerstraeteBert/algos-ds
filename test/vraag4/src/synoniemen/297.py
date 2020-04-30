def synoniemen(tekst, woordenboek):
    l = tekst.split()
    uit = ''
    for w in l:
        if w in woordenboek:
            uit += woordenboek[w] + ' '
        else:
            uit += w + ' '
            
    uit = uit[:-1]        
    return uit        