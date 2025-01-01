import re
import sys

# Token types
TOKEN_TYPES = {
    'PRINT': r'print',
    'LET': r'let',
    'IF': r'if',
    'REPEAT': r'repeat',
    'FUNCTION': r'function',
    'NUMBER': r'\d+',
    'STRING': r'".*?"',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'OPERATOR': r'[=+]',
    'BRACE_OPEN': r'\{',
    'BRACE_CLOSE': r'\}',
    'PAREN_OPEN': r'\(',
    'PAREN_CLOSE': r'\)',
    'WHITESPACE': r'\s+',
}

# Lexer: Tokenizer
def tokenize(code):
    tokens = []
    position = 0
    while position < len(code):
        match = None
        for token_type, pattern in TOKEN_TYPES.items():
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                if token_type != 'WHITESPACE':  # Ignore whitespace
                    tokens.append((token_type, match.group(0)))
                position = match.end()
                break
        if not match:
            raise SyntaxError(f"Unexpected character: {code[position]}")
    return tokens

# Parser: Simple executor
def execute(tokens):
    variables = {}

    def eval_expression(expression):
        if expression.startswith('"') and expression.endswith('"'):
            return expression[1:-1]  # Remove quotes
        elif expression.isdigit():
            return int(expression)
        elif expression in variables:
            return variables[expression]
        else:
            raise NameError(f"Undefined variable: {expression}")

    i = 0
    while i < len(tokens):
        token_type, value = tokens[i]

        if token_type == 'LET':
            var_name = tokens[i + 1][1]
            if tokens[i + 2][0] != 'OPERATOR' or tokens[i + 2][1] != '=':
                raise SyntaxError("Expected '=' after variable name")
            var_value = eval_expression(tokens[i + 3][1])
            variables[var_name] = var_value
            i += 4

        elif token_type == 'PRINT':
            to_print = eval_expression(tokens[i + 1][1])
            print(to_print)
            i += 2

        else:
            raise SyntaxError(f"Unexpected token: {token_type}")

    return variables

# Main function for command-line usage
def main():
    if len(sys.argv) < 2:
        print("Usage: apilage <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            code = file.read()
        tokens = tokenize(code)
        execute(tokens)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
