def verlaat_ploeg(naam, ploeg, overzicht):
    overzicht[ploeg].remove(naam)
    if not overzicht[ploeg]:
        del overzicht[ploeg]
    return overzicht


def vervoegt_ploeg(naam, ploeg, overzicht):
    if ploeg in overzicht.keys():
        overzicht[ploeg].append(naam)
    else:
        overzicht[ploeg] = [naam]
    return overzicht
