from intermediate import IntermediateElement
from svg_writer import SVGElement
from utils import hex_to_rgba_alpha_str, hex_to_tuple
from PIL import ImageFont

class IntermediateText(IntermediateElement):

    def to_svg(self):
        fill_color, fill_opacity = hex_to_rgba_alpha_str(self.get("fill-color"))
        stroke_color, stroke_opacity = hex_to_rgba_alpha_str(self.get("stroke-color"))

        align_vertical = self.get("align_vertical")
        dy = "0.25em"
        if align_vertical == "bottom":
            dy = "1em"

        return SVGElement("text",              
            {
                "x": self.get("x"),
                "y": self.get("y"),
                "text-anchor": self.get("text-anchor"),
                "dy": dy,
                "fill": fill_color,
                "fill-opacity": fill_opacity,
                "font-size": self.get("font-size"),
                "stroke": stroke_color,
                "stroke-opacity": stroke_opacity,
                "stroke-width": self.get("stroke-width"),
                "font-family": "Arial"
            },
            [self.get("text")])

    def draw(self, img):
        font_size = self.get("font-size")
        font = ImageFont.truetype("Pillow/Tests/fonts/DejaVuSans.ttf", font_size)

        x = self.get("x")
        y = self.get("y")
        text = self.get("text")

        if self.get("text-anchor") == "middle":
            anchor_x = "m"
        elif self.get("text-anchor") == "start":
            anchor_x = "l"
        elif self.get("text-anchor") == "end":
            anchor_x = "r"

        anchor_y = "b"
        if self.get("align_vertical") == "center":
            anchor_y = "m"
        if self.get("align_vertical") == "bottom":
            anchor_y = "t"

        stroke_width = self.get("stroke-width")

        img.text((x, y),
            text,
            font=font,
            anchor=anchor_x+anchor_y,
            fill=hex_to_tuple(self.get("fill-color")),
            stroke_fill=hex_to_tuple(self.get("stroke-color")),
            stroke_width=int(stroke_width))