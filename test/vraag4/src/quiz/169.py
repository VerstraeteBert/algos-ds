def verlaat_ploeg(naam, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(naam)
    if not inschrijvingen[ploeg]:
        del inschrijvingen[ploeg]
    return inschrijvingen


def vervoegt_ploeg(naam, ploeg, inschrijvingen):
    if not ploeg in inschrijvingen:
        inschrijvingen[ploeg] = []
    if not naam in inschrijvingen[ploeg]:
        inschrijvingen[ploeg].append(naam)
    return inschrijvingen


# print(verlaat_ploeg('Fien', 'Levies', {'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
print(vervoegt_ploeg('Els','Sinbox',{'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))