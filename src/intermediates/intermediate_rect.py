from intermediate import IntermediateElement
from svg_writer import SVGElement
from utils import rgba_alpha_to_hex

class IntermediateRect(IntermediateElement):

    def to_svg(self):
        return SVGElement("rect",
            {
                "x": self.get("x"),
                "y": self.get("y"),
                "width": self.get("width"),
                "height": self.get("height"),
                "rx": self.get("border-radius"),
                "ry": self.get("border-radius"),
                "fill": self.get("fill-color"),
                "fill-opacity": self.get("fill-opacity"),
                "stroke": self.get("stroke-color"),
                "stroke-width": self.get("stroke-width"),
                "stroke-opacity": self.get("stroke-opacity")
            })

    def draw(self, img):
        x1 = self.get("x")
        y1 = self.get("y")
        x2 = x1 + self.get("width")
        y2 = y1 + self.get("height")

        fill_color = rgba_alpha_to_hex(self.get("fill-color"), self.get("fill-opacity"))
        stroke_color = rgba_alpha_to_hex(self.get("stroke-color"), self.get("stroke-opacity"))

        img.rounded_rectangle((x1, y1, x2, y2),
            fill=fill_color,
            outline=stroke_color,
            width=int(self.get("stroke-width")),
            radius=int(self.get("border-radius")))