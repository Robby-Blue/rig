from language.syntax_exception import BadSyntaxException

def assert_type(token, expected_types):
    actual_type = token["type"]
    if isinstance(expected_types, str):
        expected_types = [expected_types]

    for expected_type in expected_types:
        if actual_type == expected_type:
            return
    
    raise BadSyntaxException(token["index"], 
        f"Expected to find {expected_types}, found {actual_type}")

def parse(tokens):
    ast = []
    idx = 0

    while idx < len(tokens):
        node = None
        token = tokens[idx]
        
        assert_type(token, "keyword")
        
        keyword = token["text"]
        if keyword == "import":
            node, idx = parse_import(tokens, idx)
        if keyword == "def":
            node, idx = parse_definition(tokens, idx)

        if node:
            ast.append(node)
        idx += 1

    return ast

def parse_import(tokens, idx):
    idx += 1

    identifier_token = tokens[idx]
    assert_type(identifier_token, "identifier")

    return {
        "type": "import_statement",
        "source": identifier_token["text"]
    }, idx

def parse_definition(tokens, idx):
    idx += 1
    identifier_token = tokens[idx]
    assert_type(identifier_token, "identifier")
    name = identifier_token["text"]

    # either 'def fig {' or 'def fig('
    idx += 1
    bracket_token = tokens[idx]
    assert_type(bracket_token, ["open_bracket", "open_curly_bracket"])
    bracket_type = bracket_token["type"]

    args = []

    if bracket_type == "open_bracket":
        idx += 1
        assert_type(tokens[idx], ["close_bracket"])
        idx += 1
        bracket_token = tokens[idx]
    
    assert_type(bracket_token, ["open_curly_bracket"])

    children = []

    if bracket_type == "open_curly_bracket":
        idx += 1
        while tokens[idx]["type"] != "close_curly_bracket":
            assert_type(tokens[idx], ["identifier"])
            child, idx = parse_object(tokens, idx)
            children.append(child)

    return {
        "type": "define_statement",
        "name": name,
        "args": args,
        "children": children
    }, idx

def parse_object(tokens, idx):
    identifier_token = tokens[idx]
    name = identifier_token["text"]

    idx += 1
    assert_type(tokens[idx], ["open_bracket"])

    idx += 1
    assert_type(tokens[idx], ["close_bracket"])

    args = []
    children = []

    idx += 1
    if tokens[idx]["type"] == "open_curly_bracket":
        idx += 1
        while tokens[idx]["type"] != "close_curly_bracket":
            assert_type(tokens[idx], ["identifier"])
            child, idx = parse_object(tokens, idx)
            children.append(child)
        idx += 1

    return {
        "type": "object_call",
        "name": name,
        "args": args,
        "children": children
    }, idx