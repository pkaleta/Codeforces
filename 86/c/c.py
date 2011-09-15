import sys

words = sys.stdin.readline()[:-1].split()

madj = "lios"
fadj = "liala"

mnoun = "etr"
fnoun = "etra"

mverb = "initis"
fverb = "inites"

m = [madj, mnoun, mverb]
f = [fadj, fnoun, fverb]

MASC = True
FEM = False

def gender(w):
    if w in m:
        return MASC
    else:
        return FEM


def check(words):
    if len(words) == 0:
        return False

    ws = []
    for w in words:
        if w[-4:] == madj or w[-4:] == fnoun:
            ws.append(w[-4:])
        elif w[-5:] == fadj:
            ws.append(w[-5:])
        elif w[-3:] == mnoun:
            ws.append(w[-3:])
        elif w[-6:] == mverb or w[-6:] == fverb:
            ws.append(w[-6:])
        else:
            return False

    if len(ws) == 1:
        return True

    for w in ws:
        if gender(w) != gender(ws[0]):
            return False

    i = 0
    if gender(ws[0]) == MASC:
        while i < len(ws) and ws[i] == madj:
            i += 1
        if i >= len(ws) or ws[i] != mnoun:
            return False
        i += 1
        while i < len(ws) and ws[i] == mverb:
            i += 1

    else:
        i = 0
        while i < len(ws) and ws[i] == fadj:
            i += 1
        if i >= len(ws) or ws[i] != fnoun:
            return False
        i += 1
        while i < len(ws) and ws[i] == fverb:
            i += 1

    if i != len(ws):
        return False

    return True


if check(words):
    print "YES"
else:
    print "NO"
