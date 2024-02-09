from typing import List, TypeVar

T = TypeVar("T")

EmptyList = "()"

def cons(atom1: T, atom2: T) -> List[T]:
    return [atom1, atom2]

def car(expr: List[T]) -> T:
    return expr[0]

def cdr(expr: List[T]) -> T:
    return expr[1]

def cadr(expr: List[T]) -> T:
    # return expr[1][0]
    return car(cdr(expr))

def cddr(expr: List[T]) -> T:
    # return exp[1][1]
    return cdr(cdr(expr))

def caddr(expr: List[T]) -> T:
    # return exp[1][1][0]
    return car(cdr(cdr(expr)))

def List(*args: T) -> T:
    val = EmptyList
    for arg in reversed(args):
        val = cons(arg, val)
    return val

def list_exp(value):
    return List("list-exp", value)

def var_exp(symbol):
    return List("var-exp", symbol)

def app_exp(f, args):
    return List("apply-exp", f, args)

def parser(expr):
    if isinstance(expr, int):
        return list_exp(expr)
    
    if isinstance(expr, str):
        return var_exp(expr)
    
    return app_exp(parser(expr[0]), List(*map(parser, expr[1:])))


if __name__ == "__main__":
    print(cons(1, 2))
    print(car(cons(1, 2)))

    print(List(1, 2, 3, 4))
    from reader import reader
    from tokenizer import tokenizer
    print(parser(reader(tokenizer("1"))))

    # print(parser(reader(tokenizer("(+ 1 2)"))))