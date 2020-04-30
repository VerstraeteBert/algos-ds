def vervoegt_ploeg(naam, ploeg, deelnemers):
    if not ploeg in deelnemers:
        deelnemers[ploeg] = []
    if not naam in deelnemers[ploeg]:
        deelnemers[ploeg].append(naam)
    return deelnemers

def verlaat_ploeg(naam, ploeg, deelnemers): #deelnemers is een dictionary
    if naam in deelnemers[ploeg]:  #deelnemers[ploeg] = dictionary[key]
        deelnemers[ploeg].remove(naam)
    #nu moeten we er enkel nog voor zorgen dat ploegen zonder deelnemers verwijdert worden
    if len(deelnemers[ploeg]) < 1:
        del deelnemers[ploeg]
    return deelnemers
