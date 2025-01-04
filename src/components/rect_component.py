from component import Component
from intermediates import IntermediateRect

class RectComponent(Component):
    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)

    def to_intermediate(self, bounds):
        border_radius = self.root().option("width") * 0.02

        margin_bounds = self.get_margin_bounds(bounds)
        x1, y1, x2, y2 = margin_bounds

        width = x2-x1
        height = y2-y1

        inner_padding = self.option("inner_padding", 0)
        layout_bounds = self.get_margin_bounds(margin_bounds, inner_padding)

        layout_intermediates = self.get_layout_intermediates(layout_bounds)
        return [IntermediateRect(self,
            {
                "x": x1,
                "y": y1,
                "width": width,
                "height": height,
                "border-radius": self.option("border_radius", 1) * border_radius,
                "fill-color": self.option("fill_color", 0x00),
                "stroke-color": self.option("color", 0xFFFFFFFF),
                "stroke-width": self.root().option("width")/300,
            }),
            *layout_intermediates]
    
    def get_name(self=None):
        return "rect"
    
    def get_args():
        return {
            "allowed": ["x", "y", "width", "height", "layer", "inner_padding", "fill_color", "color", "layout", "border_radius"],
            "positional": ["x", "y", "width", "height", "color"],
            "required": []
        }