def verlaat_ploeg(naam, ploeg, alle_inschrijvingen):
    alle_inschrijvingen[ploeg].remove(naam)     #verwijder value naam waar key = ploeg
    if not alle_inschrijvingen[ploeg]:          # if geen value for key ploeg
        del alle_inschrijvingen[ploeg]          # delete key ploeg
    return alle_inschrijvingen
    
def vervoegt_ploeg(naam, ploeg, alle_inschrijvingen):
    list = [naam]                               # create list with value naam
    if ploeg not in alle_inschrijvingen:        # if key ploeg niet bestaat
        alle_inschrijvingen[ploeg] = list       # create key/list pair 
    else:                                       # key ploeg bestaat al
        alle_inschrijvingen[ploeg].append(naam) # add value naam to list with key ploeg
    return alle_inschrijvingen
    