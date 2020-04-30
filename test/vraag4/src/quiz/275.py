def verlaat_ploeg(deeln, pnaam, dict):
    dict[pnaam].remove(deeln)
    if dict[pnaam] == []:
        del dict[pnaam]
    return dict
    
    
def vervoegt_ploeg(deeln, pnaam, dict):
    if pnaam in dict:
        dict[pnaam].append(deeln)
    else:
        dict[pnaam] = [deeln]
    return dict