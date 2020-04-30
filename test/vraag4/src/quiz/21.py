def verlaat_ploeg(naam, team, deelnemers):
        return deelnemers[team].remove(naam)
        

def vervoegt_ploeg(naam, team, deelnemers):
        return deelnemers[team].append(naam)