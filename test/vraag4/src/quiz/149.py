def verlaat_ploeg(naam, ploeg, quiz):
    quiz[ploeg].remove(naam)
    if quiz[ploeg] == []:
        del quiz[ploeg]
    return quiz

def vervoegt_ploeg(naam, ploeg, quiz):
    if not ploeg in quiz:
        quiz[ploeg] = []
    if not naam in quiz[ploeg]:
        quiz[ploeg].append(naam)
    return quiz