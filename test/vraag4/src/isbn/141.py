def overzicht(codes):
    engels = []
    frans = []
    duits = []
    japan = []
    russisch = []
    china = []
    andere = []
    fout = []
    for code in codes:
        lijst = list(code)
        if int(code[:3]) == 978 or int(code[:3]) == 979:
            o = 0
            e = 0
            for i in range(0, len(lijst)-1, 2):
                i = int(i)
                lijst[i] = int(lijst[i])
                o += lijst[i]
            for j in range(1, len(lijst), 2):
                j = int(j)
                lijst[j] = int(lijst[j])
                e += lijst[j]
            if (10-(o+3*e) % 10) % 10 == int(lijst[-1]):
                if lijst[3] == 0 or lijst[3] == 1:
                    engels.append(code)
                elif lijst[3] == 2:
                    frans.append(code)
                elif lijst[3] == 3:
                    duits.append(code)
                elif lijst[3] == 4:
                    japan.append(code)
                elif lijst[3] == 5:
                    russisch.append(code)
                elif lijst[3] == 7:
                    china.append(code)
                else:
                    andere.append(code)
            else:
                fout.append(code)
        else:
            fout.append(code)
    print(f"Engelstalige landen: {len(engels)}")
    print(f"Franstalige landen: {len(frans)}")
    print(f"Duitstalige landen: {len(duits)}")
    print(f"Japan: {len(japan)}")
    print(f"Russischtalige landen: {len(russisch)}")
    print(f"China: {len(china)}")
    print(f"Overige landen: {len(andere)}")
    print(f"Fouten: {len(fout)}")