'''
Check refactoring
'''
from Stack import ArrayStack as Stack
from splitTokens import splitTokens
from infixToPostfix import infixToPostfix

def postfixEval(tokenList):
    valStack = Stack()

    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
        elif token == '*':
            v1 = valStack.pop()
            v2 = valStack.pop()
            result = v2 * v1
            valStack.push(result)
        elif token == '/':
            v1 = valStack.pop()
            v2 = valStack.pop()
            result = v2 / v1
            valStack.push(result)
        elif token == '+':
            v1 = valStack.pop()
            v2 = valStack.pop()
            result = v2 + v1
            valStack.push(result)
        elif token == '-':
            v1 = valStack.pop()
            v2 = valStack.pop()
            result = v2 - v1
            valStack.push(result)
    return valStack.pop()



