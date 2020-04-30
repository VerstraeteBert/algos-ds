def verlaat_ploeg(deelnemer,groep,dict):
    nieuwe_samenstelling =[]
    for el in dict[groep]:
        if el != deelnemer:
            nieuwe_samenstelling.append(el)
    if nieuwe_samenstelling:
        dict[groep] = nieuwe_samenstelling
    else:
        del dict[groep]
    return dict

def vervoegt_ploeg(deelnemer, groep, dict):
    if groep in dict:
        dict[groep].append(deelnemer)
    else:
        dict[groep]=[deelnemer]
    return dict