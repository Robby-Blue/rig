from intermediate import IntermediateElement
from svg_writer import SVGElement
from utils import rgba_alpha_to_hex

class IntermediateCircle(IntermediateElement):

    def to_svg(self):
        return SVGElement("circle",
            {
                "r": self.get("radius"),
                "cx": self.get("x"),
                "cy": self.get("y"),
                "fill": self.get("fill-color"),
                "fill-opacity": self.get("fill-opacity"),
                "stroke": self.get("stroke-color"),
                "stroke-width": self.get("stroke-width"),
                "stroke-opacity": self.get("stroke-opacity")
            })

    def draw(self, img):
        x = self.get("x")
        y = self.get("y")

        fill_color = rgba_alpha_to_hex(self.get("fill-color"), self.get("fill-opacity"))
        stroke_color = rgba_alpha_to_hex(self.get("stroke-color"), self.get("stroke-opacity"))

        img.circle((x, y),
            radius=int(self.get("radius")),
            fill=fill_color,
            outline=stroke_color,
            width=int(self.get("stroke-width")))