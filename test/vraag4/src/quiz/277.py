def verlaat_ploeg(deelnemer, ploeg, woordenboek):
    if ploeg in woordenboek:
        l = woordenboek[ploeg]
        l.remove(deelnemer)
        woordenboek[ploeg] = l
        if len(l) == 0:
            del woordenboek[ploeg]
            return woordenboek
        else:
            return woordenboek

def vervoegt_ploeg(deelnemer, ploeg, woordenboek):
    if ploeg in woordenboek:
        l = woordenboek[ploeg]
        l.append(deelnemer)
        woordenboek[ploeg] = l
        return woordenboek
    else :
        l = [deelnemer]
        woordenboek[ploeg] = l
        return woordenboek