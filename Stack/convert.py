'''
Convert to infix to notaion
'''
from Stack import ArrayStack

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def convert(S):
    opStack = ArrayStack()
    answer = ''
    
    for c in S:
        if c not in "*/+-()":
           answer += c
        elif c == '(':
            opStack.push(c)
        elif c == ")":
            while opStack.peek() != "(":
                answer += opStack.pop()
            opStack.pop()
        elif (not opStack.isEmpty()) and prec.get(c) <= prec.get(opStack.peek()):
            answer += opStack.pop()
            opStack.push(c)
        else:
            opStack.push(c)
   
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer
        




if __name__ == "__main__":
    # test cases
    print(convert('(A+B)*C'))
    print(convert('a+b+c'))
    print(convert('a+b*c'))
    print(convert('a*b-c'))
    print(convert('(A+B*C)+D'))
    print(convert('(A*B-C)-D'))
    print(convert('(A*B)-(D*E+F)'))
