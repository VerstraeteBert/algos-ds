def verlaat_ploeg(naam,ploeg,woordenboek):
    naamlijst=woordenboek[ploeg]
    naamlijst.remove(naam)
    if len(naamlijst)==0:
        del woordenboek[ploeg]
    else:
        woordenboek[ploeg]=naamlijst
    return woordenboek

def vervoegt_ploeg(naam,ploeg,woordenboek):
    if ploeg in woordenboek:
        naamlijst=woordenboek[ploeg]
        naamlijst.append(naam)
        woordenboek[ploeg]=naamlijst
    else:
        lege=[]
        lege.append(naam)
        woordenboek[ploeg]=lege
    return woordenboek