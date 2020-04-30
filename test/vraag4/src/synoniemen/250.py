def synoniemen(tekst, woordenboek):
    nieuw = []
    for i in tekst.split():
        if i in woordenboek:
            nieuw.append(woordenboek[i])
        else:
            nieuw.append(i)
    return" ".join(nieuw)