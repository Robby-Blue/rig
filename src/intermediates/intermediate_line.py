from intermediate import IntermediateElement
from svg_writer import SVGElement
from utils import rgba_alpha_to_hex

class IntermediateLine(IntermediateElement):

    def to_svg(self):
        return SVGElement("line",
            {
                "x1": self.get("x1"),
                "y1": self.get("y1"),
                "x2": self.get("x2"),
                "y2": self.get("y2"),
                "stroke": self.get("color"),
                "stroke-opacity": self.get("opacity"),
                "stroke-width": self.get("width")
            })

    def draw(self, img):
        x1 = self.get("x1")
        y1 = self.get("y1")
        x2 = self.get("x2")
        y2 = self.get("y2")

        color = rgba_alpha_to_hex(self.get("color"), self.get("opacity"))
        
        img.line((x1, y1, x2+1, y2+1),
            fill=color,
            width=int(self.get("width")))