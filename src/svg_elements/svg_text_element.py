from PIL import ImageFont
from svg_writer import SVGElement

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
        elif self.get("text-anchor") == "left":
            anchor_x = "l"
        elif self.get("text-anchor") == "right":
            anchor_x = "r"

        anchor_y = "m"
        if self.get("dy") == "1em":
            anchor_y = "b"

        stroke_width = int(self.get("stroke-width"))

        img.text((x, y),
            text,
            font=font,
            anchor=anchor_x+anchor_y,
            fill=self.get("fill"),
            stroke_fill=self.get("stroke"),
            stroke_width=stroke_width)