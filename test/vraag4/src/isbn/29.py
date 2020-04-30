def uitschrijven(codes):
    d = {'0':'En'}
    for i in codes:
        o = 0
        e = 0
        for j in range(0, len(i)-1, 2):
            o += int(i[j])
            e += int(i[j+1])
        x = (10 - ((o + 3*e)%10))%10
        e = 0
        if x == i[12]:
            if i[3] == 0 or i[3] == 1:
                e += 1
            elif i[3] == 2:
                f += 1
            elif i[3] == 3:
                d += 1
            elif i[3] == 4:
                j += 1
            elif i[3] == 5:
                r += 1
            elif i[3] == 7:
                c += 1
            elif i[3] == 6 or i[3] == 8 or i[3] == 9:
                o += 1
        else:
            fo += 1
    
            
            
        