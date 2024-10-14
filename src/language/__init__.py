from language.tokenizer import tokenize
from language.parser import parse
from language.syntax_exception import BadSyntaxException

import json

def compile(file):
    with open(file, "r") as f:
        src = f.read()

        try:
            tokens = tokenize(src)
            ast = parse(tokens)
            print(json.dumps(ast, indent=2))
        except BadSyntaxException as e:
            print_error(e, src, file)

def print_error(error, src, file):
    start_index = error.start_index
    end_index = error.end_index

    line_start_index = src.rindex("\n", 0, start_index) + 1
    line_end_index = src.index("\n", start_index)

    line = src[line_start_index:line_end_index].strip()

    line_number = src[0:line_start_index].count("\n") + 1

    relative_start_index = start_index - line_start_index
    relative_end_index = end_index - line_start_index
    token_length = end_index - start_index + 1

    prefix = f"  | "
    line_prefix = f"{line_number} | "

    print(f"Error in '{file}', line {line_number}")
    print(prefix)
    print(line_prefix + line)
    print(prefix + " " * relative_start_index + "^" * token_length)
    print(error.message)

    if error.fix:
        print()
        print("Potential fix:")

        fixed_line = line[:relative_start_index] + error.fix + line[relative_end_index+1:]

        print(prefix + fixed_line)