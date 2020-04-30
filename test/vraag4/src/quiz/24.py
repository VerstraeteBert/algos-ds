def verlaat_ploeg(naam,ploeg,bib):
    (bib[ploeg]).remove(naam)
    if not bib[ploeg]:
        del bib[ploeg]
    
    return bib

def vervoegt_ploeg(naam, ploeg,bib):
    
    if ploeg in bib:
        (bib[ploeg]).append(naam)
    
    else:
        bib[ploeg] = [naam]
        
    return bib