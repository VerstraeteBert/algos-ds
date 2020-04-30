def overzicht(lijst):
    Engelstalige_landen = 0
    Franstalige_landen = 0
    Duitstalige_landen = 0
    Japan = 0
    Russischtalige_landen = 0
    China = 0
    Overige = 0
    Fouten = 0
    for j in range(len(lijst)):
        for i in len[j]:
            if i[:2] == 979 or i[:2] == 978:
                if i[3] == 0 or i[3] == 1:
                    Engelstalige_landen += 1
                elif i[3] == 2:
                    Franstalige_landen += 1
                elif i[3] == 3:
                    Duitstalige_landen += 1
                elif i[3] == 4:
                    Japan += 1
                elif i[3] == 5:
                    Russischtalige_landen += 1
                elif i[3] == 7:
                    China += 1
                else:
                    Overige+= 1
            else:
                Fouten += 1
    return('Engelstalige landen: {}'.format(Engelstalige_landen))
    ('Franstalige landen: {}'.format(Franstalige_landen))
    ('Duitstalige landen: {}'.format(Duitstalige_landen))
    ('Japan: {}'.format(Japan))
    ('Russischtalige landen: {}'.format(Russischtalige_landen))
    ('China: {}'.format(China))
    ('Overige landen: {}'.format(Overige))
    ('Fouten: {}'.format(Fouten))