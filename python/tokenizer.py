from typing import List


# transform input characters to tokens
def tokenizer(input: str) -> List[str]:
    tokens = []
    builder = ""

    for char in input:
        match char:
            case "(" | ")" | "[" | "]":
                if len(builder) > 0:
                    tokens.append(builder)
                # reset builder to empty string
                builder = ""
                tokens.append(char)
            case " " | "\t" | "\n":
                if len(builder) > 0:
                    tokens.append(builder)
                builder = ""
            case _:
                builder += char

    if len(builder) > 0:
        tokens.append(builder)
    builder = ""
    return tokens


if __name__ == "__main__":
    test1 = "(1 2 3 4)"
    assert tokenizer(test1) == ["(", "1", "2", "3", "4", ")"]

    test2 = """(this    is a
            3.14 
            (test))"""
    assert tokenizer(test2) == ["(", "this", "is", "a", "3.14", "(", "test", ")", ")"]
