def verlaat_ploeg(deelnemer, ploeg, inschrijvingen):
    deelnemers = inschrijvingen[ploeg]
    deelnemers.remove(deelnemer)
    if not deelnemers:
        del inschrijvingen[ploeg]
    else:
        inschrijvingen[ploeg] = deelnemers
    return inschrijvingen


def vervoegt_ploeg(deelnemer, ploeg, inschrijvingen):
    try:
        deelnemers = inschrijvingen[ploeg]
        deelnemers.append(deelnemer)
        inschrijvingen[ploeg] = deelnemers
    except KeyError:
        inschrijvingen[ploeg] = [deelnemer]
    return inschrijvingen


print(vervoegt_ploeg('Els', 'Sinbox',
                     {'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'],
                      'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
