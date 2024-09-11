import sys
import json

from elements import get_element_contructor
from layouts import get_layout_contructor
from renderer import svg_renderer

def read_element(src):
    element_type_name = src["type"]
    element_type = get_element_contructor(element_type_name)

    element = element_type(**src)

    if "children" in src:
        src_layout = element.option("layout", {"type": "relative"})
        layout_type_name = src_layout["type"]
        layout_type = get_layout_contructor(layout_type_name)

        layout = layout_type(**src_layout)

        element.set_layout(layout)
        for child in src["children"]:
            element.add_child(read_element(child))
    return element

def main():
    if len(sys.argv) < 3:
        print("not enough arguments:")
        print("python", sys.argv[0], "<input> <output>")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as f:
        src = json.load(f)

    svg_element = read_element(src)
    svg = svg_element.to_svg()

    if output_file.endswith("svg"):
        with open(output_file, "w") as f:
            f.write(str(svg))
    if output_file.endswith("png"):
        img = svg_renderer.render(svg)
        img.save(output_file)

if __name__ == "__main__":
    main()