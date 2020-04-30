def synoniemen (zin,w):
    zin=zin.split(" ")
    nieuwe=""
    for item in zin:
        if item in w:
            nieuwe += w[item] + " "
        else:
            nieuwe+= item + " "
    nieuwe = nieuwe.rstrip(" ")
    return nieuwe