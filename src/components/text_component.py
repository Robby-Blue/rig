from component import Component
from intermediates import IntermediateText

class TextComponent(Component):
    def __init__(self, src, variables, templates):
        src["height"] = 1
        super().__init__(src, variables, templates)

    def to_intermediate(self, bounds):
        x1, y1, _, _ = bounds

        text_anchor = "middle"
        align_vertical = "center"
        # normally youd use dominant-baseline,
        # but that doesnt work everywhere

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
                "stroke-color": self.option("outline", 0x00),
                "stroke-width": self.option("stroke_width", 1) * width_multiplier,
            })

        return [svg_element]
    
    def get_size(self, bounds=None):
        _, y1, _, y2 = bounds
        container_height = y2 - y1

        width_multiplier = self.root().option("width") / 700
        font_size = self.option("font_size", 1) * 20 * width_multiplier
        text_height = 1 * font_size

        return [0, text_height / container_height * 100]
    
    def get_name(self=None):
        return "text"
    
    def get_args():
        return {
            "allowed": ["x", "y", "layer", "width", "height", "layout", "center_h", "align_text_h", "center_v", "align_text_v", "width", "color", "outline", "font_size", "stroke_width", "text"],
            "positional": ["text", "x", "y"],
            "required": ["text"]
        }