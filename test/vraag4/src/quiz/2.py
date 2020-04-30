def verlaat_ploeg(deelnemer, ploeg, dictionary):
    dictionary[ploeg].remove(deelnemer)
    if not dictionary[ploeg]:
        del dictionary[ploeg]
    return dictionary

def vervoegt_ploeg(deelnemer, ploeg, dictionary):
    if not ploeg in dictionary:
        dictionary[ploeg] = deelnemer
    dictionary[ploeg].append(deelnemer)
    return dictionary
    
def vervoegt_ploeg(naam, ploeg, deelnemers):
    if not ploeg in deelnemers:
        deelnemers[ploeg] = []
    if not naam in deelnemers[ploeg]:
        deelnemers[ploeg].append(naam)
    return deelnemers    

    
    