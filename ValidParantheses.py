def isValid(s):
    stack = []
    for i in s:
        if i == '(' or i == '{' or i=='[':
            stack.append(i)
        elif i == ')' or i == '}' or i==']':
            if not stack:
                return False
                pop_ele = stack.pop()
                if i == ')' and pop_ele == '(':
                    return True
                if i == '}' and pop_ele == '{':
                    return True      
                if i == ']' and pop_ele == '[':
                    return True
