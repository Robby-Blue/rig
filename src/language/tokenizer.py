keywords = [
    "import",
    "def"
]

char_tokens = {
    "{": "open_curly_bracket",
    "}": "close_curly_bracket",
    "(": "open_bracket",
    ")": "close_bracket",
    ":": "colon",
    ",": "comma",
    "+": "plus_sign",
    "-": "minus_sign",
    "*": "multiplication_sign",
    "/": "division_sign"
}

def tokenize(src, file):
    src += " "

    tokens = []
    idx = 0
    while idx < len(src):
        token = None
        start_idx = idx
        char = src[idx]
        if char.isalpha():
            token, idx = read_identifier(src, idx)
        elif char == "\"":
            token, idx = read_string(src, idx)
        elif char.isdigit():
            token, idx = read_number(src, idx)
        elif char == "#":
            token, idx = read_hex(src, idx)
        else:
            if char in char_tokens:
                token = {"type": char_tokens[char]}

        if token:
            token["start_index"] = start_idx
            token["end_index"] = idx
            token["file"] = file
            tokens.append(token)
        idx += 1
    return tokens

def read_identifier(src, idx):
    start_idx = idx
    while src[idx].isalpha() or src[idx] == "_":
        idx += 1
    name = src[start_idx:idx]

    if name in ["true", "false"]:
        return {
            "type": "boolean",
            "value": name == "true"
        }, idx-1 

    return {
        "type": "keyword" if name in keywords else "identifier",
        "name": name
    }, idx-1

def read_string(src, idx):
    # TODO improve this to handle escapes
    # TODO detect and raise unclosed strings
    # and other tokens
    idx += 1
    start_idx = idx
    while src[idx] != "\"":
        idx += 1
    text = src[start_idx:idx]
    return {
        "type": "string",
        "text": text
    }, idx

def read_number(src, idx):
    # TODO improve this to handle non ints
    start_idx = idx
    while src[idx].isdigit():
        idx += 1
    num_str = src[start_idx:idx]
    return {
        "type": "number",
        "value": int(num_str)
    }, idx-1

def read_hex(src, idx):
    hex_digits = "0123456789ABCDEFabcdefg"

    idx += 1
    start_idx = idx
    while src[idx] in hex_digits:
        idx += 1
    hex_str = src[start_idx:idx]

    value = int(hex_str, 16)

    if len(hex_str) == 6:
        value = value << 8
        value = value | 0xFF

    return {
        "type": "hex",
        "value": value
    }, idx-1