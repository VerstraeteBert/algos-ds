deelnemers = {'Sinbox': ['An', 'Tom', 'Griet'],'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}

def verlaat_ploeg(naam, ploeg, deelnemers):
    deelnemers[ploeg].remove(naam)
    if  not deelnemers[ploeg]:
        del deelnemers[ploeg]
    return deelnemers

def vervoegt_ploeg(naam, ploeg, deelnemers):
    if ploeg not in deelnemers:
        deelnemers[ploeg] = []
    deelnemers[ploeg].append(naam)
    return deelnemers