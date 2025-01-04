def calculate_expression(expression, variables):
    operators = {
        "plus_sign": calculate_plus,
        "minus_sign": calculate_minus,
        "multiplication_sign": calculate_multiplication,
        "division_sign": calculate_division,
    }

    stack = []
    for token in expression:
        if token["type"] == "number":
            stack.append(token["value"])
        if token["type"] == "string":
            stack.append(token["text"])
        if token["type"] == "identifier":
            stack.append(variables[token["name"]])
        if token["type"] in operators.keys():
            func = operators[token["type"]]
            val2 = stack.pop()
            val1 = stack.pop()
            stack.append(func(val1, val2))

    return stack[0]

def calculate_plus(val1, val2):
    if isinstance(val1, str) or isinstance(val2, str):
        return str(val1) + str(val2)
    return val1+val2

def calculate_minus(val1, val2):
    if isinstance(val1, str) or isinstance(val2, str):
        return # todo add errors
    return val1-val2

def calculate_multiplication(val1, val2):
    if isinstance(val1, str) or isinstance(val2, str):
        return # todo add errors
    return val1*val2

def calculate_division(val1, val2):
    if isinstance(val1, str) or isinstance(val2, str):
        return # todo add errors
    return val1/val2

def precalculate_vars(values, variables):
    values = dict(values)
    for k, v in values.items():
        if not isinstance(v, dict) or \
            v["type"] != "expression":
            continue
        
        values[k] = calculate_expression(
            v["expression"], variables)
        
    return values