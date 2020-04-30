def verlaat_ploeg(deelnemer, ploeg, dict_ploegen):
    if ploeg in dict_ploegen:
        teamleden = dict_ploegen[ploeg]
        #print(teamleden)
        if deelnemer in teamleden:
            teamleden.remove(deelnemer)
            dict_ploegen[ploeg] = teamleden
            #print(n_teamleden)
            #print(ploeg)
            if teamleden == []:
                del dict_ploegen[ploeg]


    return dict_ploegen

def vervoegt_ploeg(deelnemer, ploeg, dict_ploegen):
    if ploeg in dict_ploegen:
        teamleden = dict_ploegen[ploeg]
        #print(teamleden)
        if deelnemer not in teamleden:
            teamleden.append(deelnemer)
            dict_ploegen[ploeg] = teamleden
            #print(n_teamleden)
            #print(ploeg)
            if teamleden == []:
                del dict_ploegen[ploeg]
    else:
        dict_ploegen[ploeg] = [deelnemer]

    return dict_ploegen