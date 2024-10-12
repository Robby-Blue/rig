keywords = [
    "import",
    "def"
]

char_tokens = {
    "{": "OPEN_CURLY_BRACKET",
    "}": "CLOSE_CURLY_BRACKET",
    "(": "OPEN_BRACKET",
    ")": "CLOSE_BRACKET",
    ":": "COLON",
    ",": "COMMA"
}

def tokenize(src):
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
        else:
            if char in char_tokens:
                token = {"type": char_tokens[char]}

        if token:
            token["index"] = start_idx
            tokens.append(token)
        idx += 1
    return tokens

def read_identifier(src, idx):
    start_idx = idx
    while src[idx].isalpha():
        idx += 1
    text = src[start_idx:idx]
    return {
        "type": "keyword" if text in keywords else "identifier",
        "text": text
    }, idx-1

def read_string(src, idx):
    # TODO improve this to handle escapes
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
        "text": int(num_str)
    }, idx-1