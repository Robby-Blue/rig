from intermediate import IntermediateElement
from svg_writer import SVGElement
from utils import hex_to_rgba_alpha_str, hex_to_tuple

class IntermediateCircle(IntermediateElement):

    def to_svg(self):
        fill_color, fill_opacity = hex_to_rgba_alpha_str(self.get("fill-color"))
        stroke_color, stroke_opacity = hex_to_rgba_alpha_str(self.get("stroke-color"))

        return SVGElement("circle",
            {
                "r": self.get("radius"),
                "cx": self.get("x"),
                "cy": self.get("y"),
                "fill": fill_color,
                "fill-opacity": fill_opacity,
                "stroke": stroke_color,
                "stroke-width": self.get("stroke-width"),
                "stroke-opacity": stroke_opacity
            })

    def draw(self, img):
        x = self.get("x")
        y = self.get("y")

        img.circle((x, y),
            radius=int(self.get("radius")),
            fill=hex_to_tuple(self.get("fill-color")),
            outline=hex_to_tuple(self.get("stroke-color")),
            width=int(self.get("stroke-width")))