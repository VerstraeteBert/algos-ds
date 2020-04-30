def synoniemen(tekst, woordenboek):
    zinnie = ''
    woorden = tekst.split()     #array met alle woorden apart
    for i in range(0,len(woorden)):
        if woorden[i] in woordenboek:
            woorden[i]= woordenboek[woorden[i]]
    for woord in woorden:
        zinnie += woord + ' '
    return zinnie.strip()    
        