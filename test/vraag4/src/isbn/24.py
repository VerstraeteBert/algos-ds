HEADERS = ["Engelstalige landen",
               "Franstalige landen",
               "Duitstalige landen",
               "Japan",
               "Russischtalige landen",
               "China",
               "Overige landen",
               "Fouten"]
MATCHES = ["01", "2", "3", "4", "5", "7", "689"]


def is_isbn13(code):
    try:
        o = sum([int(code[i]) for i in range(0, 12, 2)])
        e = sum([int(code[i]) for i in range(1, 12, 2)])

        return (10 - ((o + 3 * e) % 10)) % 10 == int(code[-1])

    except ValueError:
        return False


def overzicht(codes: str):
    counter = [0 for _ in range(len(HEADERS))]

    for code in codes:
        if not code.startswith(("978", "979")) or not is_isbn13(code):
            counter[-1] += 1
        
        else:
            ident = code[3]
            pos = next((i for i in range(len(MATCHES)) if ident in MATCHES[i]))
            
            counter[pos] += 1
    
    for i in range(len(HEADERS)):
        print(f"{HEADERS[i]}: {counter[i]}")