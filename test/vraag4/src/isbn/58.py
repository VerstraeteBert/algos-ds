def overzicht(codes):
    overz = {"Engelstalige landen": 0,
             "Franstalige landen": 0,
             "Duitstalige landen": 0,
             "Japan": 0,
             "Russischtalige landen": 0,
             "China": 0,
             "Overige landen": 0,
             "Fouten": 0
             }
    for code in codes:
        if code[0:3] == "978" or code[0:3] == "979":
            e = int()
            o = int()
            tel = 0
            for i in code:
                if tel < 12:
                    if tel % 2 == 0:
                        o += int(i)
                    else:
                        e += int(i)
                    tel += 1
            controle = (10 - (o + (3 * e)) % 10) % 10
            if controle == int(code[-1]):
                cijfer = int(code[3])
                if cijfer in (0, 1):
                    overz.update({"Engelstalige landen": overz["Engelstalige landen"] + 1})
                elif cijfer == 2:
                    overz.update({"Franstalige landen": overz["Franstalige landen"] + 1})
                elif cijfer == 3:
                    overz.update({"Duitstalige landen": overz["Duitstalige landen"] + 1})
                elif cijfer == 4:
                    overz.update({"Japan": overz["Japan"] + 1})
                elif cijfer == 7:
                    overz.update({"China": overz["China"] + 1})
                elif cijfer == 5:
                    overz.update({"Russischtalige landen": overz["Russischtalige landen"] + 1})
                else:
                    overz.update({"Overige landen": overz["Overige landen"] + 1})
            else:
                overz.update({"Fouten": overz["Fouten"] + 1})
        else:
            overz.update({"Fouten": overz["Fouten"] + 1})
    for land, aantal in overz.items():
        print(land + ":", aantal)