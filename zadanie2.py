def eval_expr(s,d={}):
    s = s.split()
    n= len(s)
    zasobnik = list()
    for i in range(n):
        if s[i] in d:
            zasobnik.append(int(d[s[i]]))
        if s[i].isdigit():
            zasobnik.append(int(s[i]))
        elif s[i]=="+":
            a=zasobnik.pop()
            b=zasobnik.pop()
            zasobnik.append(int(a+b))
        elif s[i]=="-":
            a=zasobnik.pop()
            b=zasobnik.pop()
            zasobnik.append(int(a-b))
        elif s[i]=="*":
            a=zasobnik.pop()
            b=zasobnik.pop()
            zasobnik.append(int(b*a))
        elif s[i]=="/":
            a=zasobnik.pop()
            b=zasobnik.pop()
            zasobnik.append(int(b/a))         
    return zasobnik.pop()

def to_infix(s):
    s = s.split()
    zasobnik = list()
    vyraz = ''
    for i in s:
        if not i in ['+', '-', '*', '/']:
            zasobnik.append(i)
        else:
            a = zasobnik.pop()
            b = zasobnik.pop()
            vyraz = '('+ ' ' + b + ' ' + i + ' ' + a + ' ' + ')'
            zasobnik.append(vyraz)
    return zasobnik.pop()

def to_postfix(s): #nestihol som dokončiť
    s = s.split()
    zasobnik = list()
    vyraz = ''
    temp = []
    for i in s:
        if i not in ['+', '-', '*', '/']:
            vyraz += i + ' '
        elif i == "(":
            temp.append('(')
        elif i == ")":
            temp.append(')')
        else:
            zasobnik.append(i)
    while zasobnik:
        vyraz += zasobnik.pop()
    return vyraz


