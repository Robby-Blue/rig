from component import Component
from intermediates import IntermediateText

class TextComponent(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_intermediate(self, bounds):
        x1, y1, _, _ = bounds
        
        align_h = "right"
        if self.option("center_h", False):
            align_h = "center"
        if self.has_option("align_text_h"):
            align_h = self.option("align_text_h", "")

        align_v = "bottom"
        if self.option("center_v", False):
            align_v = "center"
        if self.has_option("align_text_v"):
            align_v = self.option("align_text_v", "")

        text_anchor = "middle"
        align_vertical = "center"
        # normally youd use dominant-baseline,
        # but that doesnt work everywhere

        if align_h == "right":
            x1, _, _, _ = self.get_margin_bounds(bounds)
            text_anchor = "start"
        if align_h == "left":
            text_anchor = "end"
        if align_v == "bottom":
            _, y1, _, _ = self.get_margin_bounds(bounds)
            align_vertical = "bottom"

        width_multiplier = self.root().option("width") / 700

        svg_element = IntermediateText(self,
            {
                "text": self.option("text"),
                "x": x1,
                "y": y1,
                "text-anchor": text_anchor,
                "align_vertical": align_vertical,
                "fill-color": self.option("color", 0xFFFFFFFF),
                "font-size": self.option("font_size", 1) * 20 * width_multiplier,
                "stroke-color": self.option("outline", 0x000000FF),
                "stroke-width": self.option("stroke_width", 1.3) * width_multiplier,
            })

        return [svg_element]
    
    def get_size(self, bounds=None):
        return [0, 0]
    
    def get_name(self=None):
        return "text"
    
    def get_args():
        return {
            "allowed": ["x", "y", "layer", "width", "height", "layout", "center_h", "align_text_h", "center_v", "align_text_v", "width", "color", "outline", "font_size", "stroke-width", "text"],
            "positional": ["text", "x", "y"],
            "required": ["text"]
        }