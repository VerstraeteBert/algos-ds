def verlaat_ploeg(deelnemer,ploeg,inschrijvingen):
    deelnemers=inschrijvingen[ploeg]
    deelnemers.remove(deelnemer)
    if deelnemers != []:
        inschrijvingen[ploeg]=deelnemers
    else:
        inschrijvingen.pop(ploeg)
    return inschrijvingen

def vervoegt_ploeg(deelnemer,ploeg,inschrijvingen):
    deelnemers=[]
    if ploeg in inschrijvingen:
        deelnemers = inschrijvingen[ploeg]
        deelnemers.append(deelnemer)
        inschrijvingen[ploeg] = deelnemers
    else:
        deelnemers.append(deelnemer)
        inschrijvingen[ploeg]=list(deelnemers)
    return inschrijvingen