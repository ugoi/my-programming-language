from lark import Lark, UnexpectedInput

grammar = """
start: expression
expression: term operator expression | term
operator: "+" | "-" | "*" | "/"
term: factor | "(" expression ")"
factor: NUMBER

%import common.NUMBER
%import common.WS
%ignore WS
"""


parser = Lark(grammar, start='start', parser='lalr')

def validate(text):
    try:
        parser.parse(text)
        return True
    except UnexpectedInput:
        return False

def main():
    tests = [
        "(3 + 2) + 1 + 1",  # Expected True
        "5",    # Expected True.
        "5 +",    # Expected False.
    ]

    for test in tests:
        print(f"{test}: {validate(test)}")

if __name__ == "__main__":
    main()
