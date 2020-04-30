def histogram(stenen):
    histo={}
    for steen in stenen:
        if steen not in histo:
            histo[steen]=1
        else:
            histo[steen]+=1
    return histo  
