from typing import Tuple, TypeVar

T = TypeVar("T")

def cons(atom1: T, atom2: T) -> Tuple[T, T]:
    return (atom1, atom2)

def car(expr: Tuple[T, T]) -> T:
    return expr[0]

def cdr(expr: Tuple[T, T]) -> T:
    return expr[1]

def cadr(exp: Tuple[T, T]) -> T:
    return exp[1][0]

def cddr(exp: Tuple[T, T]) -> T:
    return exp[1][1]

def caddr(exp: Tuple[T, T]) -> T:
    return exp[1][1][0]

def List(*args: T) -> T:
    if len(args) <= 0:
        return ()
    
    first, *rest = args
    return cons(first, List(*rest))

def list_exp(value):
    return List("list-exp", value)

def symbol_exp(symbol):
    return List("symbol-exp", symbol)

def eval_exp(f, args): 
    return List("eval-exp", f, args)

def parser(expr):
    if isinstance(expr, int):
        return list_exp(expr)
    
    if expr in ["+", "-", "*", "/"]:
        return symbol_exp(expr)
    
    f, *args = expr
    return eval_exp(f, *args)


if __name__ == "__main__":
    print(cons(1, 2))
    print(car(cons(1, 2)))

    print(List(1, 2, 3, 4))