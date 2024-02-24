from typing import List, Literal, TypeVar, Any

class SyntaxToken:
    def __init__(self, val: Literal["(", ")"]) -> None:
        self.kind = "SyntaxToken"
        self.val: str = val
    def __repr__(self) -> str:
        return self.val

# "define", "+", "-", "*", "/"
class SymbolToken:
    def __init__(self, val: str) -> None:
        self.kind = "SymbolToken"
        self.val: str = val
    def __repr__(self) -> str:
        return self.val

class BooleanToken:
    def __init__(self, val: str) -> None:
        self.kind = "BooleanToken"
        self.val: bool = val
    def __repr__(self) -> str:
        return str(self.val)

class IntegerToken:
    def __init__(self, val: str) -> None:
        self.kind = "IntegerToken"
        self.val: int = val
    def __repr__(self) -> str:
        return str(self.val)

# parse source string into token string
def tokenizer(source_string: str) -> List[str]:
    tokens = []
    builder = ""
    for i in range(0, len(source_string)):
        if source_string[i] in ["(", ")"]:
            if builder:
                tokens.append(builder)
            tokens.append(source_string[i])
            builder = ""
        elif source_string[i] in [" ", "\t", "\n"]:
            if builder:
                tokens.append(builder)
            builder = ""
        else:
            builder += source_string[i]
    
    if builder:
        tokens.append(builder)
    
    return tokens

Token = IntegerToken | BooleanToken | SymbolToken | SyntaxToken

# parse token string into token type
def reader(tokens: List[str]) -> List[Token]:
    convert_tokens = []
    for token_string in tokens:
        if token_string.isdigit():
            token = IntegerToken(int(token_string))
            convert_tokens.append(token)
        elif token_string in ["(", ")"]:
            token = SyntaxToken(token_string)
            convert_tokens.append(token)
        elif token_string in ["#t", "#f"]:
            token = BooleanToken(True if token == "#t" else False)
            convert_tokens.append(token)
        else:
            token = SyntaxToken(token_string)
            convert_tokens.append(token)
    return convert_tokens

lexer = lambda source_string: reader(tokenizer(source_string))

class SingletonExpression:
    pass

class ApplyExpression:
    pass

AST = Token | List[Token] | TypeVar("AST")

# (+ (+ 3 4) (+ 11 12))

# parse token to AST
def parser(tokens: Token | List[Token]) -> AST:
    if not isinstance(tokens, list):
        return tokens
    
    ast = []
    stack = []

    for token in tokens:
        if token.val == "(":
            if len(stack) > 0:
                if len(ast) <= 0:
                    ast.extend(stack)
                else:
                    ast.append(stack)
            stack = []
        elif token.val == ")":
            if len(stack) > 0:
                if len(ast) <= 0:
                    ast.extend(stack)
                else:
                    ast.append(stack)
            stack = []
        else:
            stack.append(token)

    return ast

def interpret(ast: AST) -> Any:


t1 = "(+ (+ 3 4) (+ 11 12))"
t2 = "(+ 1 2)"
t3 = "(+ 1 (+ 2 3))"
t4 = "(+ (+ 2 3) 1)"

re = parser(lexer(t4))
print(re)