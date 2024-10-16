from language.tokenizer import tokenize
from language.parser import parse
from language.ir_generator import generate_ir
from language.syntax_exception import BadSyntaxException

import sys

def compile(file):
    with open(file, "r") as f:
        src = f.read()

        try:
            tokens = tokenize(src)
            try:
                ast = parse(tokens)
            except IndexError:
                raise BadSyntaxException(len(src)-1, len(src)+1,
                    "Unexpected EOF")
            ir = generate_ir(ast)
            return ir
        except BadSyntaxException as e:
            print_error(e, src, file)
            sys.exit(1)

def print_error(error, src, file):
    red = "\x1b[1;34;31m"
    green = "\x1b[1;34;32m"
    reset = "\x1b[0m"

    if not sys.stdout.isatty():
        red = ""
        green = ""
        reset = ""

    start_index = error.start_index
    end_index = error.end_index

    line_start_index = src.rindex("\n", 0, start_index) + 1
    line_end_index = (src+"\n").index("\n", start_index)

    orig_line = src[line_start_index:line_end_index]
    line = orig_line.lstrip()
    left_stripped = len(orig_line) - len(line)
    line = line.strip()

    start_index -= left_stripped
    end_index -= left_stripped

    line_number = src[0:line_start_index].count("\n") + 1

    relative_start_index = start_index - line_start_index
    relative_end_index = end_index - line_start_index
    token_length = end_index - start_index + 1

    prefix = " " * len(str(line_number)) + " | "
    line_prefix = f"{line_number} | "

    print(f"{red}error:{reset} bad syntax in '{file}', line {line_number}")
    print(prefix)
    print(line_prefix + line)
    print(prefix + make_arrows(relative_start_index, token_length, red) + reset)
    print(error.message)

    if error.fix:
        fixed_line = line[:relative_start_index] + green + error.fix + reset + line[relative_end_index+1:]

        fix_length = len(error.fix)

        print()
        print(green+"+ potential fix:"+reset)
        print(prefix + fixed_line)
        print(prefix + make_arrows(relative_start_index, fix_length, green) + reset)

def make_arrows(spaces, length, color):
    return " " * spaces + color + "^" * length