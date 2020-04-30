def histogram(lijst):
    lege={}
    lengte=len(lijst)
    for i in range (0,lengte,1):
        toevoegen=lijst[i]
        aantal=lijst.count(toevoegen)
        if toevoegen not in lege:
            lege[toevoegen]=aantal
    return lege

def max_gelijk(lijst1):
    lege=histogram(lijst1)
    a=lege.values()
    b=max(a)
    return b

def is_FullHouse(lijst2):
    eerste=lijst2[0]
    tel2=lijst2.count(eerste)
    if tel2!=2 and tel2!=3:
        return False
    for i in range(0,tel2,1):
        lijst2.remove(eerste)
    f=lijst2[0]
    tel3=lijst2.count(f)
    return tel2+tel3==5
    
    