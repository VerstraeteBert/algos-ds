def verlaat_ploeg(naam,ploeg,deelnemende_ploegen):
    deelnemende_ploegen[ploeg].remove(naam)
    if not deelnemende_ploegen[ploeg]:
        del deelnemende_ploegen[ploeg]
    return deelnemende_ploegen

def vervoegt_ploeg(naam,ploeg,deelnemende_ploegen):
    if not ploeg in deelnemende_ploegen:
        deelnemende_ploegen[ploeg] = []
    if not naam in deelnemende_ploegen[ploeg]:
        deelnemende_ploegen[ploeg].append(naam)
    return deelnemende_ploegen   
        