def verlaat_ploeg(naam, groep, boek):
    groep_sl = boek[groep].split()
    for speler in groep_sl:
        if speler == naam:
            del speler
    return boek

