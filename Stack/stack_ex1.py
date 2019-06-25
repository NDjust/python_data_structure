from Stack import ArrayStack

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''

    for c in S:
        if c == " ":
            continue
        elif c not in "()*+-/":
            answer += c
        else:
            if opStack.isEmpty() and c in prec.keys():
                opStack.push(c)
            else:
                if c == ")":
                    while opStack.peek() != '(':
                        answer += opStack.pop()
                    opStack.pop()
                elif c == "(":
                    opStack.push(c)
                elif prec.get(opStack.peek()) < prec.get(c):
                    opStack.push(c)
                else:
                    answer += opStack.pop()
                    opStack.push(c)
    while not opStack.isEmpty():
        answer += opStack.pop()
    return answer



if __name__ == "__main__":
    # test cases
    print(solution('(A+B)*C'))
    print(solution('a + b+ c'))
    print(solution('a+b*c'))
    print(solution('a*b-c'))
    print(solution('(A +B*C)+D'))
    print(solution('(A*B-C)-D'))
    print(solution('(A*B)-(D*E+F)'))
