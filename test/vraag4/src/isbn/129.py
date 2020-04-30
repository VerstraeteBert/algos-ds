def isISBN(code):
    if code[0:3] not in '978 979':
        return False
    x = []
    for i in range(0, 13):
        x.append(code[i])
    o = 0
    e = 0
    for i in range(0, 11, 2):
        o += int(x[i])
    for i in range(1, 12, 2):
        e += int(x[i])
    x13c = (10 - (o + 3 * e) % 10) % 10
    if x13c == int(x[12]):
        return True
    else:
        return False


def overzicht(codes):
    landen = {0: 0, 1: 0, 2: 0, 3: 0,
              4: 0, 5: 0, 6: 0, 7: 0}
    indexing = {0: 0, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 6, 7: 5, 8: 6, 9: 6}
    for index, code in enumerate(codes):
        if isISBN(code):
            land = int(code[3])
            landen[indexing[land]] += 1
        else:
            landen[7] += 1
    print(f'Engelstalige landen: {landen[0]}')
    print(f'Franstalige landen: {landen[1]}')
    print(f'Duitstalige landen: {landen[2]}')
    print(f'Japan: {landen[3]}')
    print(f'Russischtalige landen: {landen[4]}')
    print(f'China: {landen[5]}')
    print(f'Overige landen: {landen[6]}')
    print(f'Fouten: {landen[7]}')