from language.compile_exception import CompileException
from language.tokenizer import char_tokens

def assert_not_type(token, not_expected_type, message, code_fix):
    actual_type = token["type"]

    if actual_type != not_expected_type:
        return

    raise CompileException("SyntaxError", token,
        message, code_fix())

def assert_type(token, expected_types, message=None):
    actual_type = token["type"]
    if isinstance(expected_types, str):
        expected_types = [expected_types]

    for expected_type in expected_types:
        if actual_type == expected_type:
            return
    
    if not message:
        message = f"expected to find {format_types(expected_types)}, found {actual_type}"
    else:
        message = message.format(actual_type)

    raise CompileException("SyntaxError", token, message)

def format_types(types):
    types = [
        format_type(type) for type in types
    ]

    if len(types) == 1:
        return types[0]
    else:
        return ", ".join(types[:-1]) + " or " + types[-1]

def format_type(type):
    if type in list(char_tokens.values()):
        idx = list(char_tokens.values()).index(type)
        char = list(char_tokens.keys())[idx]
        return f"'{char}'"
    return type

def parse(tokens):
    ast = []
    idx = 0

    imports_done = False

    while idx < len(tokens):
        node = None
        token = tokens[idx]
        
        assert_type(token, "keyword")
        
        keyword = token["text"]
        if keyword == "import":
            if imports_done:
                raise CompileException("ArgumentError", token, 
"Can't have import after definition")

            node, idx = parse_import(tokens, idx)
        if keyword == "def":
            imports_done = True
            node, idx = parse_definition(tokens, idx)

        if node:
            ast.append(node)
        idx += 1

    return ast

def parse_import(tokens, idx):
    identifier_token, idx = read_token(tokens, idx)
    assert_not_type(identifier_token, "string",
"expected name of file to import, found string",
lambda: identifier_token["text"])
    assert_type(identifier_token, "identifier",
"expected name of file to import, found {}")

    return {
        "type": "import_statement",
        "token": identifier_token,
        "source": identifier_token["text"]
    }, idx

def parse_definition(tokens, idx):
    identifier_token, idx = read_token(tokens, idx)
    assert_type(identifier_token, "identifier",
"expected name of component, found {}")
    name = identifier_token["text"]

    # either 'def fig {' or 'def fig('
    bracket_token, idx = read_token(tokens, idx)
    assert_type(bracket_token, ["open_bracket", "open_curly_bracket"])
    bracket_type = bracket_token["type"]

    args = {}

    if bracket_type == "open_bracket":
        args, idx = parse_args(tokens, idx+1, False)

        assert_type(tokens[idx], ["close_bracket"])
        bracket_token, idx = read_token(tokens, idx)
        bracket_type = bracket_token["type"]

    assert_type(bracket_token, ["open_curly_bracket"])

    children = []

    if bracket_type == "open_curly_bracket":
        idx += 1
        while tokens[idx]["type"] != "close_curly_bracket":
            children, idx = parse_children(tokens, idx)

    return {
        "type": "define_statement",
        "token": identifier_token,
        "name": name,
        "args": args,
        "children": children
    }, idx

def parse_children(tokens, idx):
    children = []
    while tokens[idx]["type"] != "close_curly_bracket":
        assert_type(tokens[idx], ["identifier"],
"expected component, found {}")
        child, idx = parse_component(tokens, idx)
        children.append(child)
        idx += 1

    return children, idx

def parse_component(tokens, idx):
    identifier_token = tokens[idx]
    name = identifier_token["text"]

    open_token, idx = read_token(tokens, idx)
    assert_type(open_token, ["open_bracket"])

    args, idx = parse_args(tokens, idx+1)

    children = []

    if tokens[idx+1]["type"] == "open_curly_bracket":
        idx += 2
        children, idx = parse_children(tokens, idx)
        assert_type(tokens[idx], "close_curly_bracket")

    return {
        "type": "component_call",
        "token": identifier_token,
        "name": name,
        "args": args,
        "children": children
    }, idx

def parse_args(tokens, idx, allow_kwargs=True):
    args = []
    had_keyword_arg = False

    while tokens[idx]["type"] != "close_bracket":
        assert_type(tokens[idx], ["identifier", "number", "string", "hex"],
"expected value or variable name, found {}")

        is_identifier = tokens[idx]["type"] == "identifier"
        colon_follows = tokens[idx+1]["type"] == "colon"
        is_kwarg = is_identifier and colon_follows

        if is_kwarg and allow_kwargs:
            identifier_token = tokens[idx]
            arg_name = identifier_token["text"]
            colon_token, idx = read_token(tokens, idx)
            assert_type(colon_token, ["colon"])

            value, idx = parse_arg(tokens, idx+1)
            value["keyword"] = arg_name
            value["keyword_token"] = identifier_token
            args.append(value)
            had_keyword_arg = True
        else:
            start_idx = tokens[idx]["start_index"]
            value, idx = parse_arg(tokens, idx)
            end_idx = tokens[idx]["end_index"]
            value["pos"] = (start_idx, end_idx)
            args.append(value)

            if had_keyword_arg:
                raise CompileException("ArgumentError", (start_idx, end_idx),
                    "can't use position arg after keyword arg")

        next_token, idx = read_token(tokens, idx)
        assert_type(next_token, ["close_bracket", "comma"])

        if next_token["type"] == "comma":
            idx += 1

    return args, idx

def parse_arg(tokens, idx):
    value_token = tokens[idx]
    assert_type(value_token, ["string", "number", "hex", "boolean", "identifier", "comma", "close_bracket"],
"expected value, found {}")

    # `identified: ,` is treated as a true
    if value_token["type"] in ["comma", "close_bracket"]:
        value = {
            "type": "value",
            "value": True
        }
        idx -= 1

    if value_token["type"] == "string":
        value = {
            "type": "value",
            "value": value_token["text"]
        }
    if value_token["type"] in ["hex", "number", "boolean"]:
        value = {
            "type": "value",
            "value": value_token["value"]
        }
    if value_token["type"] == "identifier":
        # either a variable or a component like a layout
        if tokens[idx+1]["type"] == "open_bracket":
            value, idx = parse_component(tokens, idx)
        else:
            value = {
                "type": "arg",
                "name": value_token["text"]
            }

    return value, idx

def read_token(tokens, idx):
    idx += 1
    return tokens[idx], idx