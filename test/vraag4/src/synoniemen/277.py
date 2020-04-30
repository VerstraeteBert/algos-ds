def synoniemen(tekst, dicti):
    l = tekst.split()
    for ind, el in enumerate(l):
        for noun, syn in dicti.items():
            if noun == el:
                l[ind] = syn
    return ' '.join(l)
            
    