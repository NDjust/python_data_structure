def insert_target(L, x):
    for i, a in enumerate(L):
        if a >= x and not i:
            L = [x] + L
            break
        elif a >= x and i != len(L) - 1:
            L = L[:i] + [x] + L[i:]
            break
        elif i == len(L) - 1:
            L = L + [x]
            break
    return L


def find_target(L, x):
    r = []
    for i, a in enumerate(L):
        if a == x:
            r += [i]
    return r if r else [-1]