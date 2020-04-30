def synoniemen(string, woordenboek):
    vervangen = []
    for woord in string.split():
        if woord in woordenboek:
            vervangen.append(woordenboek[woord])
        else:
            vervangen.append(woord)
    return " ".join(vervangen)