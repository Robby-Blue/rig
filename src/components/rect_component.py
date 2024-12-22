from component import Component
from intermediates import IntermediateRect

from utils import hex_rgba_to_rgba_alpha

class RectComponent(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_intermediate(self, bounds):
        border_radius = self.root().option("width") * 0.02

        margin_bounds = self.get_margin_bounds(bounds)
        x1, y1, x2, y2 = margin_bounds

        width = x2-x1
        height = y2-y1

        inner_padding = self.option("inner_padding", 0)
        layout_bounds = self.get_margin_bounds(margin_bounds, inner_padding)

        fill_color, fill_opacity = hex_rgba_to_rgba_alpha(self.option("fill_color", "#00000000"))
        stroke_color, stroke_opacity = hex_rgba_to_rgba_alpha(self.option("color", "#FFFFFF"))

        layout_intermediates = self.get_layout_intermediates(layout_bounds)
        return [IntermediateRect(self,
            {
                "x": x1,
                "y": y1,
                "width": width,
                "height": height,
                "border-radius": border_radius,
                "fill-color": fill_color,
                "fill-opacity": fill_opacity,
                "stroke-color": stroke_color,
                "stroke-width": self.root().option("width")/300,
                "stroke-opacity": stroke_opacity
            }),
            *layout_intermediates]
    
    def get_name(self=None):
        return "rect"
    
    def get_args():
        return {
            "allowed": ["x", "y", "width", "height", "layer", "inner_padding", "fill_color", "color", "layout"],
            "positional": ["x", "y", "width", "height", "color"],
            "required": []
        }