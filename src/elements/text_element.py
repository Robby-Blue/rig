from element import Element
from svg_elements import SVGTextElement

from utils import hex_rgba_to_rgba_alpha

class TextElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_svg(self, bounds):
        x1, y1, _, _ = bounds
        
        align_h = "right"
        if self.option("center_h", False) == True:
            align_h = "center"
        if self.has_option("align_text_h"):
            align_h = self.option("align_text_h", "")

        align_v = "bottom"
        if self.option("center_v", False) == True:
            align_v = "center"
        if self.has_option("align_text_v"):
            align_v = self.option("align_text_v", "")

        text_anchor = "middle"
        dy = "0.25em"
        # normally youd use dominant-baseline,
        # but that doesnt work everywhere

        if align_h == "right":
            x1, _, _, _ = self.get_margin_bounds(bounds)
            text_anchor = "start"
        if align_h == "left":
            text_anchor = "end"
        if align_v == "bottom":
            _, y1, _, _ = self.get_margin_bounds(bounds)
            dy = "1em"

        width_multiplier = self.root().option("width") / 700

        fill_color, fill_opacity = hex_rgba_to_rgba_alpha(self.option("color", "#FFFFFF"))
        stroke_color, stroke_opacity = hex_rgba_to_rgba_alpha(self.option("outline", "#000000"))

        svg_element = SVGTextElement(self,
            {
                "x": x1,
                "y": y1,
                "text-anchor": text_anchor,
                "dy": dy,
                "fill": fill_color,
                "fill-opacity": fill_opacity,
                "font-size": int(self.option("font-size", 20) * width_multiplier),
                "stroke": stroke_color,
                "stroke-opacity": stroke_opacity,
                "stroke-width": int(self.option("stroke-width", 1.3) * width_multiplier),
                "font-family": "Arial",
                "font-weight": "bold"
            },
            [self.option("text")])

        return [svg_element]
    
    def get_size(self, bounds=None):
        return [0, 0]
    
    def get_name(self=None):
        return "text"