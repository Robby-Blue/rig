from svg_writer import SVGElement

from utils import rgba_alpha_to_hex

class SVGCircleElement(SVGElement):

    def __init__(self, src, attributes, children=None):
        super().__init__("circle", src, attributes, children)

    def render(self, img):
        x = self.get("cx")
        y = self.get("cy")

        fill_color = rgba_alpha_to_hex(self.get("fill"), self.get("fill-opacity"))
        stroke_color = rgba_alpha_to_hex(self.get("stroke"), self.get("stroke-opacity"))

        img.circle((x, y),
            radius=self.get("r"),
            fill=fill_color,
            outline=stroke_color,
            width=self.get("stroke-width"))