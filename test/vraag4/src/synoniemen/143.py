def synoniemen(tekst, woordenboek):
    z = []
    for i in tekst.split():
        if i in woordenboek:
            z.append(woordenboek[i])
        else:
            z.append(i)
    return " ".join(z)
