def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return 1
    
def associativity(c):
    if c == '^':
        return 'R'
    return 'L'

def infix_to_postfix(s):
    result = []
    stack = []

    for i in range(len(s)):
        c = s[i]

        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= '9'):
            result.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and (prec(s[i]) < prec(stack[-1]) or (prec(s[i]) == prec(stack[-1]) and associativity(s[i]) == 'L')):
                 result.append(stack.pop())
            stack.append(c)

    while stack:
        result.append(stack.pop())
    print(''.join(result))

exp = "a+b*(c^d-e)^(f+g*h)-i"
infix_to_postfix(exp)