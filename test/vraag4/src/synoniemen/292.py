def synoniemen(tekst,synoniemen):
    a=tekst.split()
    for i in range(len(a)):
        if a[i] in synoniemen:
                a[i]=synoniemen[a[i]]
    return " ".join(a)
                    
 

    
        
        