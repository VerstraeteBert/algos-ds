def gift_inschrijven(sponsoring, giften):       
    if sponsoring[0] in giften:                 
        giften[sponsoring[0]] += sponsoring[1]  
    else:                                       
        giften[sponsoring[0]] = sponsoring[1]   
    return giften                                        