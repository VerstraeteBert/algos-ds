def overzicht(codes,groepsnummer):
    fouten=0
    verzameling_van_landen=[]
    for i in range(len(codes)):
        isbn=codes[i]
        if isbn[:3] != "978" or isbn[:3] != "979":
            fouten +=1
        elif isbn[:3] == "978" or isbn[:3] == "979":
            land=groepsnummer[str(isbn[3])]
            verzameling_van_landen.append(land)
            oneven=0
            even=0
            for i in range(len(isbn)):
                if i==12:
                    x13=int(isbn[i])
                elif (i+1)%2==0:
                    even += int(isbn[i])
                elif (i+1)%2!=0:
                    oneven += int(isbn[i])
            if x13!= (10-(oneven+3*even)%10)%10:
                fouten+=1
    engeland=verzameling_van_landen.count("Engeland")
    frankrijk=verzameling_van_landen.count("Frankrijk")
    duitsland=verzameling_van_landen.count("Duitsland")
    japan = verzameling_van_landen.count("Japan")
    rusland = verzameling_van_landen.count("Rusland")
    china = verzameling_van_landen.count("china")
    overige_landen = verzameling_van_landen.count("overige landen")
    print("Engelstalige landen:", engeland)
    print("Franstalige landen:", frankrijk)
    print("Duitstalige landen:", duitsland)
    print("Japan:", japan)
    print("Rusland:", rusland)
    print("China:", china)
    print("Overige landen:", overige_landen)
    print("Fouten:", fouten)
codes = ['9789743159664', '9785301556616', '9797668174969', '9781787559554', '9780817481461', '9785130738708',
            '9798810365062', '9795345206033', '9792361848797', '9785197570819', '9786922535370', '9791978044523',
             '9796357284378', '9792982208529', '9793509549576', '9787954527409', '9797566046955', '9785239955499',
             '9787769276051', '9789910855708', '9783807934891', '9788337967876', '9786509441823', '9795400240705',
             '9787509152157', '9791478081103', '9780488170969', '9795755809220', '9793546666847', '9792322242176',
             '9782582638543', '9795919445653', '9796783939729', '9782384928398', '9787590220100', '9797422143460',
             '9798853923096', '9784177414990', '9799562126426', '9794732912038', '9787184435972', '9794455619207',
             '9794270312172', '9783811648340', '9799376073039', '9798552650309', '9798485624965', '9780734764010',
             '9783635963865', '9783246924279', '9797449285853', '9781631746260', '9791853742292', '9781796458336',
             '9791260591924', '9789367398012']
groepsnummer={'0':'Engeland','1':'Engeland','2':'Frankrijk','3':'Duitsland','4':'Japan','5':'Rusland','7':'China','6':'overige landen',"8":'overige landen','9':'overige landen'}
print(overzicht(codes,groepsnummer))

