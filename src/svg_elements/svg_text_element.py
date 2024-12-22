from PIL import ImageFont
from svg_writer import SVGElement

from utils import rgba_alpha_to_hex

class SVGTextElement(SVGElement):

    def __init__(self, src, attributes, children=None):
        super().__init__("text", src, attributes, children)

    def render(self, img):
        font_size = self.get("font-size")
        font = ImageFont.truetype("Pillow/Tests/fonts/DejaVuSans.ttf", font_size)

        x = self.get("x")
        y = self.get("y")
        text = self.children[0]

        if self.get("text-anchor") == "middle":
            anchor_x = "m"
        elif self.get("text-anchor") == "start":
            anchor_x = "l"
        elif self.get("text-anchor") == "end":
            anchor_x = "r"

        anchor_y = "b"
        if self.get("dy") == "0.25em":
            anchor_y = "m"
        if self.get("dy") == "1em":
            anchor_y = "t"

        stroke_width = self.get("stroke-width")
        fill_color = rgba_alpha_to_hex(self.get("fill"), self.get("fill-opacity"))
        stroke_color = rgba_alpha_to_hex(self.get("stroke"), self.get("stroke-opacity"))
        
        img.text((x, y),
            text,
            font=font,
            anchor=anchor_x+anchor_y,
            fill=fill_color,
            stroke_fill=stroke_color,
            stroke_width=int(stroke_width))