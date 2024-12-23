from intermediate import IntermediateElement
from svg_writer import SVGElement
from utils import hex_to_rgba_alpha_str, hex_to_tuple

class IntermediateRect(IntermediateElement):

    def to_svg(self):
        fill_color, fill_opacity = hex_to_rgba_alpha_str(self.get("fill-color"))
        stroke_color, stroke_opacity = hex_to_rgba_alpha_str(self.get("stroke-color"))

        return SVGElement("rect",
            {
                "x": self.get("x"),
                "y": self.get("y"),
                "width": self.get("width"),
                "height": self.get("height"),
                "rx": self.get("border-radius"),
                "ry": self.get("border-radius"),
                "fill": fill_color,
                "fill-opacity": fill_opacity,
                "stroke": stroke_color,
                "stroke-width": self.get("stroke-width"),
                "stroke-opacity": stroke_opacity
            })

    def draw(self, img):
        x1 = self.get("x")
        y1 = self.get("y")
        x2 = x1 + self.get("width")
        y2 = y1 + self.get("height")


        img.rounded_rectangle((x1, y1, x2, y2),
            fill=hex_to_tuple(self.get("fill-color")),
            outline=hex_to_tuple(self.get("stroke-color")),
            width=int(self.get("stroke-width")),
            radius=int(self.get("border-radius")))