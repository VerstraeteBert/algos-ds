def gift_inschrijven(sponsering,woordenboek):
    klas,gift=sponsering
    if not klas in woordenboek:
        woordenboek[klas]=0
    woordenboek[klas]+=gift
    return woordenboek