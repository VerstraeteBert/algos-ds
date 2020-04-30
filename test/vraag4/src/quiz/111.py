def verlaat_ploeg(naam, ploeg, inschrijvngen_dict):
        inschrijvngen_dict[ploeg].remove(naam)
        if inschrijvngen_dict[ploeg] == []:
                del inschrijvngen_dict[ploeg]
        return inschrijvngen_dict

def vervoegt_ploeg(naam, ploeg, inschrijvngen_dict):
        try: 
                inschrijvngen_dict[ploeg].append(naam)
                return inschrijvngen_dict
        except KeyError:
                inschrijvngen_dict.update({ploeg: [naam]})
                return inschrijvngen_dict