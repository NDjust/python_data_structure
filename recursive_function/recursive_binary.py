def recursive_binary(L, target_numm, lower, upper):
    '''
    by using recursive function 
    install binary search algorithms.
    '''
    if l >= u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return recursive_binary(L, x, lower, mid - 1)

    else:
        return recursive_binary(L, x, mid + 1, upper)


if __name__ == "__main__":
    L = [2, 3, 5, 6, 9, 11, 15]
    x = 6
    l = 0
    u = 6
    print(recursive_binary(L, x, l, u))
