import sys
import json

import language

from elements import get_element_contructor
from layouts import get_layout_contructor
from renderer import svg_renderer

def read_element(src, templates, variables):
    src = dict(src)
    element_type_name = src["type"]

    for key, val in src.items():
        if not isinstance(val, dict):
            continue
        if val["type"] != "arg":
            continue
        src[key] = variables[val["name"]]

    if element_type_name == "template":
        template_name = src["name"]
        template = dict(templates[template_name])
        variables = src
        return read_element(template, templates, variables)
    else:
        element_type = get_element_contructor(element_type_name)

    element = element_type(**src)

    if "children" in src:
        src_layout = element.option("layout", {"type": "relative"})
        layout_type_name = src_layout["type"]
        layout_type = get_layout_contructor(layout_type_name)

        layout = layout_type(**src_layout)

        element.set_layout(layout)
        for child in src["children"]:
            element.add_child(read_element(child, templates, variables))
    return element

def main():
    if len(sys.argv) < 3:
        print("not enough arguments:")
        print("python", sys.argv[0], "<input> <output>")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if input_file.endswith(".json"):
        with open(input_file, "r") as f:
            src = json.load(f)
    if input_file.endswith(".rig"):
        src = language.compile(input_file)

    svg_element = read_element(src["fig"], src, {})
    svg = svg_element.to_svg()

    if output_file.endswith("svg"):
        with open(output_file, "w") as f:
            f.write(str(svg))
    if output_file.endswith("png"):
        img = svg_renderer.render(svg)
        img.save(output_file)

if __name__ == "__main__":
    main()