'''
Check refactoring
'''
from Stack import ArrayStack as Stack
from splitTokens import splitTokens

def infixToPostfix(tokenList):

    prec = {
        '*': 3, '/': 3,
        '+': 2, '-': 2,
        '(': 1,
    }

    opStack = Stack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        else:
            if opStack.isEmpty() and token in prec.keys():
                opStack.push(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                while opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                opStack.pop()
            elif prec.get(opStack.peek()) < prec.get(token):
                opStack.push(token)
            else:
                postfixList.append(opStack.pop())
                opStack.push(token)
        
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList

def test():
    result = []
    test_case = ['1+2 * (3+1)', '1+3*4', "(1 + 2) * (2 *3)", "(3 * 2) - (1 + 2 * 3)", '7 * (9 - (3 + 2))',
                 '5 + 3', '(1 + 2) * (3 + 4)', '7 * (9-(3+2))', '3 + (2 - 3 * (1 + 2 + ( 4 * 2 - 1)))']
    for tc in test_case:
        tokens = splitTokens(tc)
        result += [infixToPostfix(tokens)]
    return result


if __name__ == "__main__":
    print(test())
