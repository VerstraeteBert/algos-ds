def gift_inschrijven(lijst, woordenboek):
    if lijst[0] in woordenboek:
        woordenboek[lijst[0]] = woordenboek[lijst[0]] + lijst[1]
    else:
        woordenboek[lijst[0]] = lijst[1]
    return woordenboek