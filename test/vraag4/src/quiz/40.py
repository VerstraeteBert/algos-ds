def verlaat_ploeg(wie,waar,dict):
    list = dict[waar]
    list.remove(wie)
    if len(list)==0:
        del dict[waar]
    return dict
def vervoegt_ploeg(wie,waar,dict):
    add=0
    try:
        list = dict[waar]
        add=1
    except:
        dict[waar]=[wie]
        list = dict[waar]
    if add==1:
        list.append(wie)
        dict[waar]=list
    return dict