def synoniemen(t, woordenboek):
    t = t.split()
    n = ""
    for woord in t:
        if woord in woordenboek:
            n += woordenboek[woord] + " "
        else:
            n += woord + " "
    return (n[:len(n) - 1])