def isbn(code):
    if len(code) != 13:
        return False
    if code[:3] != "978" and code[:3] != "979":
        return False
    even = code[::2]
    oneven = code[1::2]
    someven = 0
    somoneven = 0
    for i in range(6):
        cijfer = int(even[i])
        someven += cijfer
        cijfer = int(oneven[i])
        somoneven += cijfer
    controle = (10 - (someven + 3 * somoneven) % 10) % 10
    return controle == int(even[6])


def overzicht(codes):
    landcodes = {"0": "Engelstalige landen", "1": "Engelstalige landen", "2": "Franstalige landen",
                 "3": "Duitstalige landen", "4": "Japan", "5": "Russischtalige landen", "7": "China",
                 "6": "Overige landen", "8": "Overige landen", "9": "Overige landen"}
    foutief = "Fouten"
    overzicht = {}
    for landtype in landcodes.values():
        overzicht[landtype] = 0
    overzicht[foutief] = 0
    for c in codes:
        if isbn(c):
            overzicht[landcodes[c[3]]] += 1
        else:
            overzicht[foutief] += 1
    for landtype, aantal in overzicht.items():
        print("{}: {}".format(landtype, aantal))


boeken = ['9789743159664', '9785301556616', '9797668174969', '9781787559554', '9780817481461', '9785130738708',
          '9798810365062', '9795345206033', '9792361848797', '9785197570819', '9786922535370', '9791978044523',
          '9796357284378', '9792982208529', '9793509549576', '9787954527409', '9797566046955', '9785239955499',
          '9787769276051', '9789910855708', '9783807934891', '9788337967876', '9786509441823', '9795400240705',
          '9787509152157', '9791478081103', '9780488170969', '9795755809220', '9793546666847', '9792322242176',
          '9782582638543', '9795919445653', '9796783939729', '9782384928398', '9787590220100', '9797422143460',
          '9798853923096', '9799562126426', '9787184435972', '9783811648340', '9799376073039', '9798552650309',
          '9798485624965', '9780734764010', '9783635963865', '9783246924279', '9797449285853', '9781631746260',
          '9791853742292', '9781796458336', '9791260591924', '9789367398012']
overzicht(boeken)
