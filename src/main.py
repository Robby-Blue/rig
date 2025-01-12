from PIL import Image, ImageDraw

import os
import sys

import language

from svg_writer import SVGElement
from component import Component

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

    with open(input_file, "r") as f:
        src = "\n" + f.read()

    src = language.compile(src, input_file)

    root_component = Component.read_child_component(src["fig"], {}, src)
    
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