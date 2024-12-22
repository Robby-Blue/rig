import sys
import json

import language

from components import get_component_contructor
from layouts import get_layout_contructor
from renderer import svg_renderer

def read_component(src, templates, variables):
    src = dict(src)
    component_type_name = src["type"]

    for key, val in src.items():
        if not isinstance(val, dict):
            continue
        if val["type"] != "arg":
            continue
        src[key] = variables[val["name"]]

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

    root_component = read_component(src["fig"], src, {})
    svg = root_component.to_svg()

    if output_file.endswith("svg"):
        with open(output_file, "w") as f:
            f.write(str(svg))
    if output_file.endswith("png"):
        img = svg_renderer.render(svg)
        img.save(output_file)

if __name__ == "__main__":
    main()