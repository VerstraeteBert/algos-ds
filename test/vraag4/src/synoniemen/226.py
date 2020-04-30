def synoniemen(tekst, wb):
    
    tekstlijst = tekst.split(' ')
    for i in tekstlijst:
        if i in wb:
            index = tekstlijst.index(i)
            tekstlijst.pop(index)
            tekstlijst.insert(index,wb[i])
    nieuwe_zin = ' '.join(tekstlijst)
    
    return nieuwe_zin

