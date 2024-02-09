from typing import List, TypeAlias
from ast import literal_eval

def tokenizer_augment(string: str, accumulator: str) -> List[str]:
    if not string and not accumulator:
        return []
    if not string and accumulator:
        return [accumulator]

    char, *string = string
    if char in ["(", "[", ")", "]"] and accumulator:
        return [accumulator, char] + tokenizer_augment(string, "")
    
    if char in ["(", "[", ")", "]"] and not accumulator:
        return [char] + tokenizer_augment(string, "")
    
    if char in [" ", "\t", "\n"] and accumulator:
        return [accumulator] + tokenizer_augment(string, "")
    
    if char in [" ", "\t", "\n"] and not accumulator:
        return tokenizer_augment(string, "")

    return tokenizer_augment(string, accumulator+char)

def tokenizer(string):
    return tokenizer_augment(string, "")

RecursiveList: TypeAlias = str | int | List["RecursiveList"]

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def reader(tokens: List[str]) -> RecursiveList:
    # ill formed parenthesis not taken care yet
    stack = []
    for token in tokens:
        if token in ["]", ")"]:
            temp_list = []
            while stack:
                token = stack.pop(-1)
                if token in ["[", "("]:
                    break
                temp_list = [token, *temp_list]
            stack.append(temp_list)
        else:
            if is_float(token):
                stack.append(float(token))
            elif is_int(token):
                stack.append(int(token))
            else:
                stack.append(token)

    return stack

if __name__ == "__main__":
    c1 = """(this    is a
    3.14 
    (test))"""
    # re = tokenizer(c1)
    # print(re)

    c2 = "(this is (a) ((list test 1.2)))"
    re = reader(tokenizer(c2))
    print(re)