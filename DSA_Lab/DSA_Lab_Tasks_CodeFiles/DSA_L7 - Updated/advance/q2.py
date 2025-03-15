import operator

def evaluate(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    stack, postfix = [], []
    
    for token in expression.split():
        if token.isdigit():
            postfix.append(int(token))
        else:
            while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                postfix.append(stack.pop())
            stack.append(token)
    
    while stack:
        postfix.append(stack.pop())
    
    eval_stack = []
    for token in postfix:
        if isinstance(token, int):
            eval_stack.append(token)
        else:
            b, a = eval_stack.pop(), eval_stack.pop()
            eval_stack.append(ops[token](a, b))
    
    return eval_stack.pop()

print(evaluate("3 + 5 * 2"))
