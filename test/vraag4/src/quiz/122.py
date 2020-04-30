def verlaat_ploeg(naam, ploeg, plogen):
    x=plogen[ploeg]
    x.remove(naam)
    if len(x)<1:
        plogen.pop(ploeg)
    return plogen
    
    
def vervoegt_ploeg(naam, ploeg, ploegen):
    if ploegen.get(ploeg)!=None:
     x=ploegen[ploeg]
     x.append(naam)
    else:
         
     ploegen[ploeg]=[naam] 
    
        
    
    return ploegen