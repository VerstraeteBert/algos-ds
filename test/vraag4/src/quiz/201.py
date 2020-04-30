def verlaat_ploeg(naam, ploeg, verzameling):
    teampie = verzameling[ploeg]
    teampie.remove(naam)

    if teampie != []:
        verzameling[ploeg] = teampie
        return verzameling
    else:
        del verzameling[ploeg]
        return verzameling


def vervoegt_ploeg(naam, ploeg, verzameling):
    if ploeg in verzameling:
        teampie = verzameling[ploeg]
        teampie.append(naam)
        verzameling[ploeg] = teampie
    else:
        verzameling[ploeg] = [naam]

    return verzameling
