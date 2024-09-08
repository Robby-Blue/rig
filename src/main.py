import sys
import json

from elements import get_element_contructor
from layouts import get_layout_contructor

def read_element(src):
    element_type_name = src["type"]
    element_type = get_element_contructor(element_type_name)

    element = element_type(**src)

    if "children" in src:
        src_layout = src["layout"]
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

    with open(sys.argv[1], "r") as f:
        src = json.load(f)

    svg_element = read_element(src)
    svg = str(svg_element)
    with open(sys.argv[2], "w") as f:
        f.write(svg)

if __name__ == "__main__":
    main()