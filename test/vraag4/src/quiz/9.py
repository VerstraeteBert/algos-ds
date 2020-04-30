def verlaat_ploeg(deelnemer, ploeg, inschrijvingen):
    spelers = inschrijvingen[ploeg]
    spelers.remove(deelnemer)
    if inschrijvingen[ploeg] == []:
        del inschrijvingen[ploeg]
    return inschrijvingen
print(verlaat_ploeg('Fien','Levies',{'Sinbox': ['An', 'Griet', 'Els'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))


def vervoegt_ploeg(deelnemer, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        spelers = inschrijvingen[ploeg]
        spelers.append(deelnemer)
    else:
        inschrijvingen[ploeg] = deelnemer.split()
    return inschrijvingen