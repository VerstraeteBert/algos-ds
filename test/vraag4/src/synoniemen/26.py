def synoniemen(zin, bib):
    deel = zin.split()
    n_zin = []
    for char in deel:
        if char in bib:
            char = bib[char]
            
        n_zin.append(char)
            
    return " ".join(n_zin)
        
        