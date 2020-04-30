def synoniemen(zin, dictionarie):


    woorden = zin.split()

    lengte = len(woorden)

    new = ''
    a = ''

    for i in range(lengte):
        arg = woorden[i]
        for woord in dictionarie:
            if woord == arg:
                new += dictionarie[woord] + ' '
                a = arg
        if a != arg:
            new += arg + ' '
        a = ''
        
    new = new.rstrip()

    return new