def verlaat_ploeg(deelnemer, team, inschrijvingen):
    inschrijvingen[team].remove(deelnemer)
    if len(inschrijvingen[team]) == 0:
        del inschrijvingen[team]
    return inschrijvingen
    
def vervoegt_ploeg(deelnemer, team, inschrijvingen):
    try:
        inschrijvingen[team].append(deelnemer)
    except KeyError:
        inschrijvingen[team] = [deelnemer]
    return inschrijvingen