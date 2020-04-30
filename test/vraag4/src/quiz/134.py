def verlaat_ploeg(deelnemers, ploegnaam, dictionairy):
    dictionairy[ploegnaam].remove(deelnemers)
    if dictionairy[ploegnaam] == []:
        del dictionairy[ploegnaam]
    return dictionairy

def vervoegt_ploeg(deelnemers, ploegnaam, dictionairy):
    if ploegnaam in dictionairy:
        dictionairy[ploegnaam].append(deelnemers)
    else:
        dictionairy[ploegnaam] = []
        dictionairy[ploegnaam].append(deelnemers)
    return dictionairy