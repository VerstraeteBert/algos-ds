def overzicht(lijst): #procedure
    Engelstalige = 0
    Franstalige = 0
    Duitstalige = 0
    Japan = 0
    Russischtalige = 0
    China = 0
    Overige = 0
    Fouten = 0
    for string in lijst:
        if string[:3] == "978" or string[:3] == "979":
            if string[3] in "01":
                Engelstalige += 1
            elif string[3] in "2":
                Franstalige += 1
            elif string[3] in "3":
                Duitstalige += 1
            elif string[3] in "4":
                Japan += 1
            elif string[3] in "5":
                Russischtalige += 1
            elif string[3] in "7":
                China += 1
            else:
                Overige += 1
        else:
            Fouten += 1
    print("Engelstalige landen:",Engelstalige)
    print("Franstalige landen:", Franstalige)
    print("Duitstalige landen:", Duitstalige)
    print("Japan:",Japan)
    print("Russischtalige landen:",Russischtalige)
    print("China:",China)
    print("Overige landen:",Overige)
    print("Fouten:",Fouten)
