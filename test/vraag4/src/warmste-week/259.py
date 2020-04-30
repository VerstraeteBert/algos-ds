def gift_inschrijven(klas_bedrag, inhoud):
    klas = klas_bedrag[0]
    klas_bedrag_dict = {klas_bedrag[0] : klas_bedrag[1]}
    if klas_bedrag[0] in inhoud:
        inhoud[klas] += float(klas_bedrag[1])
        
  
    else:
        inhoud.update(klas_bedrag_dict)
    return inhoud