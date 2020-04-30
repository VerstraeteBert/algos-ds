def synoniemen(tekst, woordenboek):
    woorden = tekst.split()
    for i in range(len(woorden)):
        if woorden[i] in woordenboek:
            woorden[i] = woordenboek[woorden[i]]
    return " ".join(woorden)

def synoniem (tekst, woordenboek):
    nieuwezin=[]