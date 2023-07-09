from typing import List

# atom -> string
# atom -> List[string]
# [atom1, atom2, atom3]

# iterative implementation using stack
def reader(tokens: List[str]) -> List[str]:
    if len(tokens) == 0:
        return []
    
    if len(tokens) == 1:
        raise Exception("unmatched brackets")

    if tokens[0] != "[":
        raise Exception("expect [")
    
    if tokens[-1] != "]":
        raise Exception("expect ]")

    # strip leading and trailing brackets
    tokens = tokens[1:-1]
    if len(tokens) == 0:
        return []
    
    result = []
    i = 0
    open_bracket = 0
    open_index = -1

    while i < len(tokens):
        token = tokens[i]
        if token == "[":
            open_bracket += 1
            if open_index == -1:
                open_index = i
        elif token == "]":
            open_bracket -= 1
            if open_bracket == 0 and open_index != -1:
                nested_read = reader(tokens[open_index:i+1])
                result.append(nested_read)
                open_bracket = 0
                open_index = -1
        else:
            if open_index == -1:
                result.append(token)
        
        i += 1

    return result

if __name__ == "__main__":
    # good form
    # test1 = ["[", "a", "b", "]"]
    # print(reader(test1))
    # assert reader(test1) == ["a", "b"]

    # test2 = ["[", "a", "[", "b", "]", "c", "]"]
    # print(reader(test2))
    # assert reader(test2) == ["a", ["b"], "c"]

    # test3 = ["[", "[", "a", "]", "[", "b", "]", "c", "]"]
    # print(reader(test3))
    # assert reader(test3) == [["a"], ["b"], "c"]

    # test4 = ["[", "[", "[", "a", "]", "]", "[", "b", "]", "c", "]"]
    # print(reader(test4))
    # assert reader(test4) == [[["a"]], ["b"], "c"]

    test5 = ["[", "]"]
    assert reader(test5) == []

    # ill formed