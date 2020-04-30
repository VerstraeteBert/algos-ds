def overzicht(codes):
    uit = {'Engelstalige landen':0, 'Franstalige landen':0, 'Duitstalige landen':0, 'Japan':0, 'Russischtalige landen':0, 'China':0, 'Overige landen':0, 'Fouten':0}
    
    for c in codes:
        l = list(c)
        
        o = 0
        e = 0
        for i in range(6):
            o += int(l[2*i])
            e += int(l[2*i+1])
        
        contr = (10-(o+3*e) %10)%10
        if int(contr) != int(l[-1]):
            uit['Fouten'] += 1
            
        elif l[3] == '0' or l[3] == '1':
            uit['Engelstalige landen'] += 1
        elif l[3] == '2':
            uit['Franstalige landen'] += 1
        elif l[3] == '3':
            uit['Duitstalige landen'] += 1
        elif l[3] == '4':
            uit['Japan'] += 1
        elif l[3] == '5':
            uit['Russischtalige landen'] += 1
        elif l[3] == '7':
            uit['China'] += 1
        elif l[3] == '6' or l[3] == '8' or l[3] == '9':
            uit['Overige landen'] += 1
        
        l = []
    for i in uit:
        print(str(i) + ': ' + str(uit[i]))            
            