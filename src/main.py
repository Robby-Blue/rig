from PIL import Image, ImageDraw

import os
import sys
import json

import language

from svg_writer import SVGElement
from components import get_component_contructor
from layouts import get_layout_contructor

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

def read_component(src, templates, variables):
    src = dict(src)
    component_type_name = src["type"]

    for k, v in src.items():
        if not isinstance(v, dict) or \
            v["type"] != "expression":
            continue
        src[k] = calculate_expression(v["expression"], variables)

    if component_type_name == "template":
        template_name = src["name"]
        template = dict(templates[template_name])
        variables = src
        return read_component(template, templates, variables)
    else:
        component_type = get_component_contructor(component_type_name)

    component = component_type(**src)

    if "children" in src:
        src_layout = component.option("layout", {"type": "relative"})
        layout_type_name = src_layout["type"]
        layout_type = get_layout_contructor(layout_type_name)

        layout = layout_type(**src_layout)

        component.set_layout(layout)
        for child in src["children"]:
            component.add_child(read_component(child, templates, variables))
    return component

def main():
    if len(sys.argv) < 2:
        print("not enough arguments:")
        print("python", sys.argv[0], "<input> <optional output>")
        return
    
    input_file = sys.argv[1]
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        output_file = input_file
        if "." in os.path.basename(output_file):
            output_file = output_file[:output_file.rindex(".")]
        output_file += ".svg"

    src = language.compile(input_file)

    root_component = read_component(src["fig"], src, {})
    intermediate = root_component.to_intermediate()
    intermediate["children"].sort(key=lambda x: x.src.layer)

    if output_file.endswith("svg"):
        svg_code = to_svg(intermediate)
        with open(output_file, "w") as f:
            f.write(svg_code)
    if output_file.endswith("png"):
        img = to_bitmap(intermediate)
        img.save(output_file)

def to_svg(intermediate):
    root_children = [c.to_svg() for c in intermediate["children"]]
    root = SVGElement("svg", {
        "width": intermediate["width"],
        "height": intermediate["height"],
        "xmlns": "http://www.w3.org/2000/svg"
    }, root_children)
    return str(root)

def to_bitmap(intermediate):
    img = Image.new(mode="RGBA", size=(intermediate["width"], intermediate["height"]))
    draw = ImageDraw.Draw(img)

    for element in intermediate["children"]:
        element.draw(draw)
    
    return img

if __name__ == "__main__":
    main()