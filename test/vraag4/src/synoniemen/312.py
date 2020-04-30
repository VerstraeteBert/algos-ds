def synoniemen(tekst, synoniemen):              
    nieuwezin = []                              
    for i in tekst.split():                     
        if i in synoniemen:                     
            nieuwezin.append(synoniemen[i])     
        else:                                   
            nieuwezin.append(i)                 
                                                
    return " ".join(nieuwezin)                  