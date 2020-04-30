def verlaat_ploeg(speler, ploeg, geheel):
    groepsleden = list(geheel[ploeg])
    groepsleden.remove(speler)
    if not groepsleden:
        del geheel[ploeg]
    else:
        geheel[ploeg] = groepsleden
    return geheel


def vervoegt_ploeg(speler, ploeg, geheel):
    if not ploeg in geheel:
        geheel[ploeg] = []
    if not speler in geheel[ploeg]:
        geheel[ploeg].append(speler)
    return geheel


