def gift_inschrijven(donatie, boekhouding):
    try:
        boekhouding[donatie[0]] += donatie[1]
    except KeyError:
        boekhouding[donatie[0]] = donatie[1]
    return boekhouding