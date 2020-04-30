def gift_inschrijven(loop,woordenboek):
    klas = loop[0]
    if klas in woordenboek:
        oud = woordenboek[klas]
        nieuw = oud + loop[1]
        woordenboek[klas] = nieuw
        return woordenboek
    else:
        woordenboek[klas] = loop[1]
        return woordenboek