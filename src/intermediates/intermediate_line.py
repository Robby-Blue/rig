from intermediate import IntermediateElement
from svg_writer import SVGElement
from utils import hex_to_rgba_alpha_str, hex_to_tuple

class IntermediateLine(IntermediateElement):

    def to_svg(self):
        stroke_color, stroke_opacity = hex_to_rgba_alpha_str(self.get("stroke-color"))

        return SVGElement("line",
            {
                "x1": self.get("x1"),
                "y1": self.get("y1"),
                "x2": self.get("x2"),
                "y2": self.get("y2"),
                "stroke": stroke_color,
                "stroke-opacity": stroke_opacity,
                "stroke-width": self.get("width")
            })

    def draw(self, img):
        x1 = self.get("x1")
        y1 = self.get("y1")
        x2 = self.get("x2")
        y2 = self.get("y2")

        img.line((x1, y1, x2+1, y2+1),
            fill=hex_to_tuple(self.get("color")),
            width=int(self.get("width")))