def gift_inschrijven( bijdrage, alles):
    if bijdrage[0] in alles:
        alles[bijdrage[0]] += bijdrage[1]
    else:
        alles[bijdrage[0]] = bijdrage[1]
    return alles