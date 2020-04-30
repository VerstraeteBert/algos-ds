def vervoegt_ploeg(naam,ploeg,dic):
    try:
        dic[ploeg] = dic[ploeg] + [naam]
    except KeyError:
        dic[ploeg] = [naam]
    return dic

def verlaat_ploeg(naam,ploeg,dic):
    lijst = dic[ploeg]
    if len(lijst) ==1: #de persoon die wordt verwijderd is de enige, heel de ploeg verwijderen 
        del dic[ploeg] #verwijder ploeg 
    else:
        lijst.remove(naam)
        dic[ploeg] = lijst
    return(dic)