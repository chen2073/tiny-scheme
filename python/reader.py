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
    # count the number of nested brackets
    open_bracket = 0
    # first nested open bracket location/index
    open_index = None

    while i < len(tokens):
        token = tokens[i]
        if token == "[":
            open_bracket += 1
            if open_index == None:
                open_index = i
        elif token == "]":
            open_bracket -= 1
            if open_bracket == 0 and open_index != None:
                nested_read = reader(tokens[open_index : i + 1])
                result.append(nested_read)
                open_bracket = 0
                open_index = None
        else:
            if open_index == None:
                result.append(token)

        i += 1

    if open_bracket != 0 or open_index != None:
        raise Exception("ill formed expression: missing closed brackets")

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

    # test5 = ["[", "]"]
    # assert reader(test5) == []

    test6 = ["[", "this", "is", "[", "a", "]", "[", "[", "list", "]", "]", "]"]
    print(reader(test6))
    assert reader(test6) == ["this", "is", ["a"], [["list"]]]

    # ill formed
    test7 = ["[", "this", "is", "[", "a", "]", "[", "[", "list", "]", "]"]
    assert reader(test6) != ["this", "is", ["a"], [["list"]]]