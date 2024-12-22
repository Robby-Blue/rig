from PIL import Image, ImageDraw

import sys
import json

import language

from svg_writer import SVGElement
from components import get_component_contructor
from layouts import get_layout_contructor

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