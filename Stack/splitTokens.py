def splitTokens(exprStr)-> list:
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ': # ignore blank
            continue
        if c in '0123456789': # number case
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing: # sign case
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)
    return tokens



