# https://dodona.ugent.be/nl/courses/264/series/2288/exercises/933472639

def isISBN13(code):
    if not(isinstance(code, str) and len(code) == 13 and code.isdigit()):
        return False
    if code[:3] not in ("978", "979"):
        return False
    ctrl = sum(int(code[i]) * (3 if i % 2 else 1) for i in range(12))
    return str((10 - (ctrl % 10)) % 10) == code[12]


def overzicht(codes):
    groups = [0] * 11
    for code in codes:
        if isISBN13(code):
            groups[int(code[3])] += 1
        else:
            groups[10] += 1

    print(f"Engelstalige landen: {groups[0] + groups[1]}"
          f"\nFranstalige landen: {groups[2]}"
          f"\nDuitstalige landen: {groups[3]}"
          f"\nJapan: {groups[4]}"
          f"\nRussischtalige landen: {groups[5]}"
          f"\nChina: {groups[7]}"
          f"\nOverige landen: {groups[6] + groups[8] + groups[9]}"
          f"\nFouten: {groups[10]}")
