def is_ISBN(nummer):
    laatst = str(nummer)[-1]
    nummer = str(nummer)[:len(str(nummer))-1]
    nummer = int(nummer)
    volgnummer = 1
    o = 0
    e = 0
    for getal in str(nummer):
        if volgnummer % 2 == 1:
            o += int(getal)
        elif volgnummer % 2 == 0:
            e += int(getal)
        volgnummer += 1

    controle = (o+(3*e))%10
    controle = (10 - controle) % 10

    if controle == int(laatst) and int(str(nummer)[:3]) in (978, 979):

        return True
    else:
        return False

def overzicht(list):
    landen = {"Engelstalige landen": 0, "Franstalige landen": 0, "Duitstalige landen": 0, "Japan": 0, "Russischtalige landen": 0,  "China": 0,  "Overige landen": 0, "Fouten": 0}
    for i in list:
        if is_ISBN(i) == False:
            landen["Fouten"] += 1

        elif int(i[3]) in (0,1):
            landen["Engelstalige landen"] += 1

        elif int(i[3]) == 2:
            landen["Franstalige landen"] += 1

        elif int(i[3]) == 3:
            landen["Duitstalige landen"] += 1

        elif int(i[3]) == 4:
            landen["Japan"] += 1

        elif int(i[3]) == 5:
            landen["Russischtalige landen"] += 1

        elif int(i[3]) == 7:
            landen["China"] += 1

        else:
            landen["Overige landen"] += 1

    for i in landen:
        print(i+":", landen[i])