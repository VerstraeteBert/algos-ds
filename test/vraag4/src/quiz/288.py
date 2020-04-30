def verlaat_ploeg(naam, ploeg, deelnemers):  #deelnemers is de volledige dictionary
    deelnemers[ploeg].remove(naam)                 #naam is de value, en ploeg is de key van het item
    if  not deelnemers[ploeg]:
        del deelnemers[ploeg]                                  # als er geen namen in de ploeg zijn, moet ploeg weg
    return deelnemers
    
def vervoegt_ploeg(naam, ploeg, deelnemers):
    if not ploeg in deelnemers:              #staat in de opgave: zo maak je een nieuwe ploeg aan door ze te 
        deelnemers[ploeg] = []                  #benoemen met een lege lijst
    if not naam in deelnemers[ploeg]: 
        deelnemers[ploeg].append(naam)
    return deelnemers    
