def synoniemen(tekst, woordenboek):
    woorden = tekst.split() #je maakt er een lijst van
    for i in range(len(woorden)): #je overloopt elk woord door de aantallen van de lijst te nemen
        if woorden[i] in woordenboek: #als het woord uit de lijst op plaat i ook in woordenboek voorkomt
            woorden[i] = woordenboek[woorden[i]] #dan wordt het woord uit de lijst od ide plaats vervangen door het woord uit woordenboek
    return " ".join(woorden)