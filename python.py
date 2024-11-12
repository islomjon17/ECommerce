import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def tokenize(expression):
    token_specification = [
        ('TAG',    r'<[a-zA-Z_][\w]*>'),     # Tags
        ('NUMBER', r'\d+(\.\d*)?'),          # Integers or decimals
        ('FUNC',   r'[a-zA-Z_]\w*'),         # Function names
        ('OP',     r'[+\-*/]'),              # Arithmetic operators
        ('LPAREN', r'\('),                   # Parentheses
        ('RPAREN', r'\)'),
        ('SKIP',   r'[ \t]+'),               # Skip spaces/tabs
        ('MISMATCH', r'.'),                  # Any other characters
    ]
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    tokens = []
    for match in re.finditer(token_regex, expression):
        type_ = match.lastgroup
        value = match.group()
        if type_ == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif type_ == 'SKIP':
            continue
        tokens.append(Token(type_, value))
    return tokens

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def parse(tokens):
    def parse_expression(index):
        if tokens[index].type == 'NUMBER':
            node = Node(tokens[index].value)
            return node, index + 1
        elif tokens[index].type == 'OP':
            node = Node(tokens[index].value)
            left, index = parse_expression(index + 1)
            right, index = parse_expression(index)
            node.children = [left, right]
            return node, index
        elif tokens[index].type == 'FUNC':
            node = Node(tokens[index].value)
            index += 1
            if tokens[index].type == 'LPAREN':
                arguments = []
                index += 1
                while tokens[index].type != 'RPAREN':
                    arg, index = parse_expression(index)
                    arguments.append(arg)
                    if tokens[index].type == 'OP':
                        index += 1
                node.children = arguments
                return node, index + 1
        return None, index

    ast, _ = parse_expression(0)
    return ast

def evaluate(node):
    if node.value in ['+', '-', '*', '/']:
        if len(node.children) != 2:
            raise ValueError(f"Operator {node.value} requires 2 arguments.")
        left = evaluate(node.children[0])
        right = evaluate(node.children[1])
        return calculate(node.value, left, right)
    elif node.value == 'sqrt':
        if len(node.children) != 1:
            raise ValueError("sqrt requires 1 argument.")
        return calculate(node.value, evaluate(node.children[0]))
    else:
        return node.value

def calculate(op, *args):
    if op == '+':
        return args[0] + args[1]
    elif op == '-':
        return args[0] - args[1]
    elif op == '*':
        return args[0] * args[1]
    elif op == '/':
        if args[1] == 0:
            raise ZeroDivisionError("Division by zero")
        return args[0] / args[1]
    elif op == 'sqrt':
        return args[0] ** 0.5
    else:
        raise ValueError(f"Unknown operation: {op}")

if __name__ == "__main__":
    while True:
        try:
            expression = input("Enter an expression (or 'quit' to exit): ")
            if expression.lower() == 'quit':
                break
            tokens = tokenize(expression)
            ast = parse(tokens)
            result = evaluate(ast)
            print("Result:", result)
        except (ValueError, ZeroDivisionError) as e:
            print("Error:", e)
