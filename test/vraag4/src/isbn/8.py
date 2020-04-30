def overzicht(codes):
    boeken_per_taal = {'Engelstalige landen:':0,'Franstalige landen:':0,'Duitstalige landen:':0,'Japan:':0,'Russischtalige landen:':0,'China:':0,'Overige landen:':0,'Fouten:':0,}
    for isbn in codes:
        isbn_ok = False
        isbn_str = str(isbn)
        laatste_cijfer = int(isbn_str[-1])
        cijfers_voor_0 = isbn_str[:12:2]
        waarde_0 = 0
        for i in cijfers_voor_0:
             waarde_0 += int(i)
        cijfers_voor_e = isbn_str[1::2]
        waarde_e = 0
        for i in cijfers_voor_e:
            waarde_e += int(i)
        x_13 = (10-((waarde_0 + 3*waarde_e) % 10)) % 10
        if x_13 == laatste_cijfer:
            isbn_ok = True
        landcijfer = int(isbn_str[3])


        if isbn_ok == True and (int(isbn_str[:3]) == 978 or int(isbn_str[:3]) == 979):
            if landcijfer == 0 or landcijfer == 1:
                boeken_per_taal['Engelstalige landen:'] += 1
            elif landcijfer == 2:
                boeken_per_taal['Franstalige landen:'] += 1
            elif landcijfer == 3:
                boeken_per_taal['Duitstalige landen:'] += 1
            elif landcijfer == 4:
                boeken_per_taal['Japan:'] += 1
            elif landcijfer == 5:
                boeken_per_taal['Russischtalige landen:'] += 1
            elif landcijfer == 7:
                boeken_per_taal['China:'] += 1
            else:
                boeken_per_taal['Overige landen:'] += 1
        else:
            boeken_per_taal['Fouten:'] += 1

    for land, aantal in boeken_per_taal.items():
        print(land, aantal)
