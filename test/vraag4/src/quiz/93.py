def verlaat_ploeg(naam, ploeg, dictionary):


    for groep in dictionary:
        if ploeg == groep:
            namen = dictionary[groep]
            lengte = len(namen)
            for i in range(lengte):
                if naam == namen[i]:
                    namen.remove(namen[i])
                    dictionary[groep] = namen

    for groep in dictionary:
        if dictionary[groep] == []:
            del dictionary[groep]

    return dictionary