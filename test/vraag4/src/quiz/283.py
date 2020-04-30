def verlaat_ploeg(deelnemer,ploeg,inschrijvingen):
    inschrijvingen[ploeg]= inschrijvingen[ploeg].remove(deelnemer)
    return inschrijvingen