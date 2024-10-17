from elements import get_element_contructor
from layouts import get_layout_contructor
from language.compile_exception import CompileException
import language
import os

def generate_ir(ast):
    ir = {}
    definitions = {}

    for node in ast:
        if node["type"] == "import_statement":
            import_file(node, ast)

    for node in ast:
        if node["type"] == "define_statement":
            name, args = definition_get_args(node)
            definitions[name] = args

    for node in ast:
        if node["type"] == "define_statement":
            transpile_definition(node, ir, definitions)

    return ir

def import_file(import_call, ast):
    base_name = import_call["source"]
    file_names = [base_name, f"{base_name}.rig"]

    found_name = None

    for file_name in file_names:
        if os.path.isfile(file_name):
            found_name = file_name

    if not found_name:
        raise CompileException("FileError", import_call["token"],
    "file to import not found")

    _, new_ast = language.file_to_ast(found_name)
    ast += new_ast

def definition_get_args(definition_node):
    component_name = definition_node["name"]
    
    allowed_args = []
    for arg in definition_node["args"]:
        allowed_args.append(arg["name"])

    return component_name, allowed_args

def transpile_definition(definition_node, ir, definitions):
    component_name = definition_node["name"]

    children_ir = []
    for child_node in definition_node["children"]:
        children_ir.append(transpile_component(child_node, definitions))

    if len(children_ir) > 1:
        raise CompileException("ComponentError", definition_node["token"],
            "can't have multiple components in the root")

    ir[component_name] = children_ir[0]

def transpile_component(component_node, definitions):
    component_name = component_node["name"]

    ir = {
        "type": component_name,
        "children": []
    }

    component = get_element_contructor(component_name)
    if component:
        args = component.get_args()
    else:
        if not component_name in definitions:
            raise CompileException("UnknownComponentError", component_node["token"],
    "called component is not defined")
        defined_args = definitions[component_name]
        args = {
            "allowed": defined_args,
            "positional": defined_args,
            "required": defined_args,
        }
        ir["type"] = "template"
        ir["name"] = component_name

    args_ir = transpile_args(component_node, args)
    for k, v in args_ir.items():
        ir[k] = v
   
    for child_node in component_node["children"]:
        ir["children"].append(transpile_component(child_node, definitions))

    return ir

def transpile_args(parent_node, component_args):
    ast_args = parent_node["args"]

    args_ir = {}

    for i, arg in enumerate(ast_args):
        if "keyword" in arg:
            keyword = arg["keyword"]
        else:
            if i >= len(component_args["positional"]):
                raise CompileException("ArgumentError", arg["pos"],
    "too many args given")
            keyword = component_args["positional"][i]
        if keyword not in component_args["allowed"]:
            raise CompileException("ArgumentError", arg["keyword_token"],
    "keyword argument not allowed for component")
        if keyword in args_ir.keys():
            raise CompileException("ArgumentError", arg["keyword_token"],
    "keyword argument already given before")

        if arg["type"] == "value":
            args_ir[keyword] = arg["value"]
        elif arg["type"] == "arg":
            args_ir[keyword] = {"name": arg["name"], "type": "arg"}
        elif arg["type"] == "component_call":
            args_ir[keyword] = transpile_arg_component(arg)

    for required_arg in component_args["required"]:
        if required_arg not in args_ir:
            raise CompileException("ArgumentError", parent_node["token"],
    f"required argument {required_arg} not given")

    return args_ir

def transpile_arg_component(ast_arg_component):
    name = ast_arg_component["name"]
    ir = {
        "type": name
    }

    component = get_layout_contructor(name)
    if not component:
        return
    args = component.get_args()

    args_ir = transpile_args(ast_arg_component, args)

    for k, v in args_ir.items():
        ir[k] = v

    return ir