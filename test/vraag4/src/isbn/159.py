def overzicht(codes):
    info = {"english": 0, "french": 0, "duits": 0, "japon": 0, "poetin_vuile_communist": 0, "namaak": 0, "overig": 0,
            "fout": 0}

    for code in codes:
        if len(code) < 13 or code[0:3] not in "978 979":
            info["fout"] += 1
        else:
            o = 0
            e = 0
            for i in range(len(code) - 1):
                if i % 2 == 0:
                    o += int(code[i])
                else:
                    e += int(code[i])

            x13 = (10 - (o + 3 * e) % 10) % 10

            if x13 == int(code[-1]):
                if int(code[3]) == 0 or int(code[3]) == 1:
                    info["english"] += 1
                elif int(code[3]) == 2:
                    info["french"] += 1
                elif int(code[3]) == 3:
                    info["duits"] += 1
                elif int(code[3]) == 4:
                    info["japon"] += 1
                elif int(code[3]) == 5:
                    info["poetin_vuile_communist"] += 1
                elif int(code[3]) == 7:
                    info["namaak"] += 1
                else:
                    info["overig"] += 1
            else:
                info["fout"] += 1

    print("Engelstalige landen:", info["english"])
    print("Franstalige landen:", info["french"])
    print("Duitstalige landen:", info["duits"])
    print("Japan:", info["japon"])
    print("Russischtalige landen:", info["poetin_vuile_communist"])
    print("China:", info["namaak"])
    print("Overige landen:", info["overig"])
    print("Fouten:", info["fout"])

