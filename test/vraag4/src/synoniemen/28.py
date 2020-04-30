def synoniemen(tekst, synoniemwoordenboek):
    woorden = ''
    for woord in tekst.split():
        if woord in synoniemwoordenboek:
            woorden += (synoniemwoordenboek[woord] + ' ')
        else:
            woorden += (woord +' ')
    return woorden.strip()