def overzicht(codes):
    i = 0
    landen = {"Engelstalige landen: ": 0,
              "Franstalige landen: ": 0,
              "Duitstalige landen: ": 0,
              "Japan: ": 0,
              "Russischtalige landen: ": 0,
              "China: ": 0,
              "Overige landen: ": 0,
              "Fouten: ": 0,
              }
    while i < len(codes):
        code = list(codes[i])
        code = list(map(int, code))
        # print(code)
        o = code[0] + code[2] + code[4] + code[6] + code[8] + code[10]
        # print(o)
        e = code[1] + code[3] + code[5] + code[7] + code[9] + code[11]
        # print(e)
        check = (10 - (o + (3 * e)) % 10) % 10
        if check == code[12]:
            if code[3] == 0 or code[3] == 1:
                landen["Engelstalige landen: "] += 1
            elif code[3] == 2:
                landen["Franstalige landen: "] += 1
            elif code[3] == 3:
                landen["Duitstalige landen: "] += 1
            elif code[3] == 4:
                landen["Japan: "] += 1
            elif code[3] == 5:
                landen["Russischtalige landen: "] += 1
            elif code[3] == 7:
                landen["China: "] += 1
            else:
                landen["Overige landen: "] += 1
        else:
            landen["Fouten: "] += 1
        i += 1
    print("Engelstalige landen: " + str(landen["Engelstalige landen: "]) +
          "\nFranstalige landen: " + str(landen["Franstalige landen: "]) +
          "\nDuitstalige landen: " + str(landen["Duitstalige landen: "]) +
          "\nJapan: " + str(landen["Japan: "]) +
          "\nRussischtalige landen: " + str(landen["Russischtalige landen: "]) +
          "\nChina: " + str(landen[""]) +
          "\nOverige landen: " + str(landen["Overige landen: "]) +
          "\nFouten: " + str(landen["Fouten: "])
          )
    