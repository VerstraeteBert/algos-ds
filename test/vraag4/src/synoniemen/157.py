def synoniemen(zin, dictionary):
    lijstwoorden = zin.split()
    for index, woord in enumerate(lijstwoorden):
        if woord in dictionary:
            synoniem = dictionary[woord]
            lijstwoorden[index] = synoniem
    tekst = ' '.join(lijstwoorden)
    return tekst
