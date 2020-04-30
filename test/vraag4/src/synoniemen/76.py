def synoniemen(zin, d):
    eindzin = str()
    
    for i in range(len(zin)):
        n = 0
        ind = 0
        if zin[i].isspace():
            if n == 0:
                woord = zin[:i]
                n += 1
                ind = i
                if 'woord' in d.keys():
                    eindzin += d['woord'] + ' '
                else:
                    eindzin += woord + ' '
            elif i != len(zin)-1:
                woord = zin[ind+1:i]
                ind = i
                if 'woord' in d.keys():
                    eindzin += d['woord'] + ' '
                else:
                    eindzin += woord + ' '
        if i == len(zin)-1:
            woord = zin[ind:]
            if 'woord' in d.keys():
                eindzin += d['woord']
            else:
                eindzin += woord
    return eindzin
                
                
                