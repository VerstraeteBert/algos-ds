def verlaat_ploeg(naam, ploeg, dic):
    team=dic[ploeg]
    team2=[]
    for i in team:
        if not i==naam:
            team2+=[i]
    dic[ploeg]=team2
    if team2==[]:
        del dic[ploeg]
    return dic
def vervoegt_ploeg(naam, ploeg, dic):
    if ploeg in dic:
        team=dic[ploeg]
        team+=[naam]
        dic[ploeg]=team
    else:
        dic[ploeg]=[naam]
    return dic