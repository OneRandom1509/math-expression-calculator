def convert(s): #converts infix expression to postfix expression

    n = '' #number string
    o = '' #operator string
    e = [] #expression list
    priority = {'^':2, '**':2, '*':1, '/':1, '//':1, '%':1, '+':0, '-':0} #priority list of operators
    stack = [] #stack for operators
    result = '' #final expression string

    for i in range(len(s)):
        if s[i].isdigit():
            n+=s[i] #storing each digit until an operator is met
            if o!= '':
                e.append(o) #appending the operator before the number 
                o = ''
        else:
            if s[i] != ')' and s[i] != '(':
                o+=s[i] #adding operator
                if s[i+1].isdigit():
                    if n!='':
                        e.append(n) #appending the number before the operator to the expression list
                    if o!='':
                        e.append(o) #appending operator to the expression list
                    n = ''
                    o = ''
            else:
                if n!='':
                    e.append(n) #appending the number before the left bracket
                if o != '':
                    e.append(o) #appending the operator before the right bracket
                n = ''
                o = ''
                e.append(s[i]) #appending the bracket
    if n!='':
        e.append(n) #appending the last number in the expression
    for i in e:
        if i.isdigit():
            result += i + ' ' #adding the number to the final expression

        elif i == '(':
            stack.append(i) #adding the left bracket to the stack

        elif i == ')': #popping operators from the stack and added to the final expression until a left bracket is met
            for a in range(len(stack)):
                op = stack.pop()
                if op != '(':
                    result += op + ' '
                else:
                    break

        else: #in case of operators other than brackets
            if stack == []: #if no operators have been previously added to the stack
                stack.append(i)
            else:
                for b in range(len(stack)): #popping operators from the stack until an operator having lower priority is met
                    if stack[-1] != '(':
                        if priority[i] <= priority[stack[-1]]: #checks if the priority of the operator is lesser than or equal to the priority of the last operator in the stack
                            result += stack.pop() + ' '
                    else:
                        break
                stack.append(i) #adding the operator after all operators having higher or same priority have been added to the final expression
    for i in range(len(stack)):
        result += stack.pop() + ' ' #adding the remaining operators to the final expression
    return result


def evaluate(s): #evaluates a postfix expression

    e = s.strip().split() #gives a list having numbers and operators as elements
    stack = [] #stack for numbers

    for i in e:
        if i.isdigit(): 
            stack.append(int(i)) #adding numbers to the stack

        else: #if the element is an operator, pop two numbers from the stack, perform the operation and push the result to the stack
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(b + a)
            elif i == '-':
                stack.append(b - a)
            elif i == '*':
                stack.append(b * a)
            elif i == '/':
                stack.append(b / a)
            elif i == '//':
                stack.append(b // a)
            elif i == '%':
                stack.append(b % a)
            elif i == '**' or i == '^':
                stack.append(b ** a)
    return stack[0] #final result 
        
s = input("Enter a mathematical expression: ")
expression = convert(s)
print(expression)
result = evaluate(expression)
print(f"{s} = {result}")