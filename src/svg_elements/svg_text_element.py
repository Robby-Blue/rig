from PIL import ImageFont
from svg_writer import SVGElement

fnt = ImageFont.truetype("Pillow/Tests/fonts/DejaVuSans.ttf", 20)

class SVGTextElement(SVGElement):

    def __init__(self, src, attributes, children=None):
        super().__init__("text", src, attributes, children)

    def render(self, img):
        x = self.get("x")
        y = self.get("y")
        text = self.children[0]

        if self.get("text-anchor") == "middle":
            anchor_x = "m"
        elif self.get("text-anchor") == "left":
            anchor_x = "l"
        elif self.get("text-anchor") == "right":
            anchor_x = "r"

        anchor_y = "m"
        if self.get("dy") == "1em":
            anchor_y = "b"

        img.text((x, y),
            text,
            font=fnt,
            anchor=anchor_x+anchor_y)