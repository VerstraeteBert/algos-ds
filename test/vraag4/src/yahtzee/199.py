def som(stenen):
    som=sum(stenen)
    return som
    
def is_Yathzee(stenen):
    laagste, hoogste=min(stenen), max(stenen)
    if laagste==hoogste:
        return True
    return False
    
def is_grote_straat(stenen):
    stenen.sort()
    for i in range(len(stenen)-1): #voor 1 2 3 4 5 overloop je tot 4
        if not(stenen[i]+1==stenen[i+1]):
            return False
    return True
def histogram(stenen):
    stenen.sort()
    histogram={}
    for i in range(len(stenen)):
        ogen=stenen[i]
        if ogen in histogram:
            histogram[ogen]+=1
        else:
            histogram[ogen]=1
    return histogram
def max_gelijk(stenen):
    histogram2=histogram(stenen) #functie hierboven gebruiken
    grootste=max(histogram2.values())
    return grootste

def is_FullHouse(stenen):
    histogram2=histogram(stenen)
    aantallen=sorted(histogram2.values(), reverse=True) #de frequenties van hoog naar laag
    if aantallen[0]==3 and aantallen[1]==2:
        return True
    return False
#skip grootste score wwant kleine straat is een complexe oef   