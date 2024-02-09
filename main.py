def tokenizer(string):
    retval = []
    current = ""
    for i in range(len(string)):
        if string[i] in ["(", "[", ")", "]"]:
            if current:
                retval.append(current)
            current = ""
            retval.append(string[i])
        elif string[i] in [" ", "\t", "\n"]:
            if current:
                retval.append(current)
            current = ""
        else:
            current += string[i]
    if current:
        retval.append(current)
    return retval

def tokenizer1(string):
    pass

def reader(texp):
    current = None
    stack = []
    for item in texp:
        if item.isdigit():
            if current is not None:
                current.append(eval(item))
            else:
                current = eval(item)
        elif item in ["[", "("]:
            if current is not None:
                stack.append(current)
            current = []
        elif item in ["]", ")"]:
            if stack:
                stack[-1].append(current)
                current = stack.pop(-1)
            else:
                pass
        else:
            if current is not None:
                current.append(item)
            else:
                current = item
    return current

EmptyList = "()"

def cons(item1, item2):
    return [item1, item2]

def car(exp):
    return exp[0]

def cdr(exp):
    return exp[1]

def cadr(exp):
    return exp[1][0]

def cddr(exp):
    return exp[1][1]

def caddr(exp):
    return exp[1][1][0]

def List(*args):
    "Create a linked-list of items"
    retval = EmptyList
    for arg in reversed(args):
        retval = cons(arg, retval)
    return retval

def List2(*args):
    if len(args) <= 0:
        return EmptyList
    return cons(args[0], *args[1:])

def lit_exp(value):
    return List("lit-exp", value)

def var_exp(symbol):
    return List("var-exp", symbol)

def app_exp(f, args):
    return List("apply-exp", f, args)

def parser(rexp):
    if isinstance(rexp, int):
        return lit_exp(rexp)
    elif isinstance(rexp, str):
        return var_exp(rexp)
    else:
        return app_exp(parser(rexp[0]), List(*map(parser, rexp[1:])))
    
def scalc_parse(string):
    return parser(reader(tokenizer(string)))

def evaluator(expr):
    if car(expr) == "lit-exp":
        return cadr(expr)
    elif car(expr) == "var-exp":
        return cadr(expr) ## for now, return symbol
    elif car(expr) == "apply-exp":
        return evaluator_apply(evaluator(cadr(expr)), Map(evaluator, caddr(expr)))
    else:
        raise Exception("invalid ast: %s" % expr)

def evaluator_apply(op, operands):
    if op == "print":
        Print(operands)
    if op == "+":
        return car(operands) + cadr(operands)
    if op == "-":
        return car(operands) - cadr(operands)
    if op == "*":
        return car(operands) * cadr(operands)
    if op == "//":
        return car(operands) // cadr(operands)
    else:
        raise Exception("unknown apply operator: %s" % op)
        
def Map(f, slist):
    if slist == EmptyList:
        return EmptyList
    else:
        return cons( f(car(slist)), Map(f, cdr(slist))) ## recursive!
    
def Print(slist):
    if slist == EmptyList:
        return
    else:
        print(car(slist))
        Print(cdr(slist))

def scalc(string):
    return evaluator(scalc_parse(string))

if __name__ == "__main__":
    # re = parser(reader(tokenizer("1")))
    # print(re)
    # re = parser(reader(tokenizer("(+ 1 2)")))
    # print(re)
    # re = scalc_parse("652362")
    # print(re)
    # re = scalc("(print 1 2 3)")
    # print(re)
    re = scalc("(+ 1 2)")
    print(re)
    re = scalc("(- 1 2)")
    print(re)
    re = scalc("(* 1 2)")
    print(re)
    re = scalc("(// 1 2)")
    print(re)
    re = scalc("(// 1 0)")
    print(re)