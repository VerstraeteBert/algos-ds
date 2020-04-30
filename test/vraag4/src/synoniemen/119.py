def synoniemen(tekst, woordenboek):
    nieuw = ""
    for a in tekst.split():
        if a in woordenboek:
            nieuw += (woordenboek[a] + " ")
        else:
            nieuw += (a + " ")
    einde = nieuw[:-1]
    return einde