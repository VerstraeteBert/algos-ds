def gift_inschrijven(tuple, dictionairy):
    if tuple[0] in dictionairy:
        dictionairy[tuple[0]] += tuple[1]

    else:
        dictionairy[tuple[0]] = tuple[1]
    return dictionairy