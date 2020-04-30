def histogram(stenen):
    dic = {}
    for i in sorted(stenen):
        a = stenen.count(i)
        dic[i] = a
    return dic
    
def max_gelijk(stenen):
    dic = histogram(stenen)
    max = 0
    for i in dic:
        if dic[i] > max:
            max = dic[i]
    return max