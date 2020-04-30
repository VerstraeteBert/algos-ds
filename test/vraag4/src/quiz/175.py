def verlaat_ploeg(deelnemer, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(deelnemer)     # bij het opvragen van een bepaalde ploeg uit de dictionary wordt (key) een lijst met de deelnemers terug gegeven (value). In deze lijst gaan we de deelnemer verwijderen via remove()
    if not inschrijvingen[ploeg]:               # als de ploeg maar uit 1 iemand bestond en deze persoon werd in vorige stap uit de dictionary verwijderd dan zal de ploeg uit een lege lijst bestaan. Lege lijsten zijn False bij if-voorwaarde.
        del inschrijvingen[ploeg]
    return inschrijvingen


def vervoegt_ploeg(deelnemer, ploeg, inschrijvingen):
    if ploeg not in inschrijvingen:             # de ploeg bestaat nog niet
        inschrijvingen[ploeg] = [deelnemer]     # nieuwe ploeg met deelnemer toevoegen aan dictionary. Let op: deelnemer tussen [] schrijven want zo wordt een lijst gevormd
    if deelnemer not in inschrijvingen[ploeg]:  # deelnemer mag geen 2 keer voorkomen in de ploeg
        inschrijvingen[ploeg].append(deelnemer)
    return inschrijvingen