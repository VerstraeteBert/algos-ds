def synoniemen(zin, woorden_boek):
    zin_list = zin.split()
    for woord in zin_list:
        if woord in woorden_boek:
            nieuw_woord = woorden_boek.get(woord)
            index = zin_list.index(woord)
            zin_list.remove(woord)
            zin_list.insert(index, nieuw_woord)
    nieuwe_zin = " ".join(zin_list)
    return nieuwe_zin