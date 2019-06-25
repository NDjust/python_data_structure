from splitTokens import splitTokens
from infixToPostfix import infixToPostfix
from postfixEval import postfixEval


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

def test():
    result = []
    eval_r = []
    test_case = ['5 + 3', '(1 + 2) * (3 + 4)', '7 * (9-(3+2))', '3 + (2 - 3 * (1 + 2 + ( 4 * 2 - 1)))']
    for tc in test_case:
        result += [solution(tc)]
        eval_r += [eval(tc)]
    return "result : {} \neval: {}".format(result, eval_r)

if __name__ == "__main__":
    print(test())
