from svg_writer import SVGElement

from utils import rgba_alpha_to_hex

class SVGRectElement(SVGElement):

    def __init__(self, src, attributes, children=None):
        super().__init__("rect", src, attributes, children)

    def render(self, img):
        x1 = self.get("x")
        y1 = self.get("y")
        x2 = x1 + self.get("width")
        y2 = y1 + self.get("height")

        fill_color = rgba_alpha_to_hex(self.get("fill"), self.get("fill-opacity"))
        stroke_color = rgba_alpha_to_hex(self.get("stroke"), self.get("stroke-opacity"))

        img.rounded_rectangle((x1, y1, x2, y2),
            fill=fill_color,
            outline=stroke_color,
            width=self.get("stroke-width"),
            radius=self.get("rx"))