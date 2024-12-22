from intermediate import IntermediateElement
from svg_writer import SVGElement
from utils import rgba_alpha_to_hex
from PIL import ImageFont

class IntermediateText(IntermediateElement):

    def to_svg(self):
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
                "fill": self.get("fill-color"),
                "fill-opacity": self.get("fill-opacity"),
                "font-size": self.get("font-size"),
                "stroke": self.get("stroke-color"),
                "stroke-opacity": self.get("stroke-opacity"),
                "stroke-width": self.get("stroke-width"),
                "font-family": "Arial",
                "font-weight": "bold"
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
        fill_color = rgba_alpha_to_hex(self.get("fill-color"), self.get("fill-opacity"))
        stroke_color = rgba_alpha_to_hex(self.get("stroke-color"), self.get("stroke-opacity"))
        
        img.text((x, y),
            text,
            font=font,
            anchor=anchor_x+anchor_y,
            fill=fill_color,
            stroke_fill=stroke_color,
            stroke_width=int(stroke_width))