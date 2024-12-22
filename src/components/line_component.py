from component import Component
from intermediates import IntermediateLine

from utils import hex_rgba_to_rgba_alpha

class LineComponent(Component):
    def __init__(self, **kwargs):
        if "width" in kwargs:
            kwargs["line_width"] = kwargs["width"]

        kwargs["x"] = kwargs["x1"]
        kwargs["y"] = kwargs["y1"]
        kwargs["width"] = kwargs["x2"] - kwargs["x1"]
        kwargs["height"] = kwargs["y2"] - kwargs["y1"]

        super().__init__(**kwargs)

    def to_intermediate(self, bounds):
        base_width = self.root().option("width") * 0.005
        width = self.option("line_width", 1) * base_width

        x1, y1, x2, y2 = bounds

        color, opacity = hex_rgba_to_rgba_alpha(self.option("color", "#FFFFFF"))

        layout_intermediates = self.get_layout_intermediates(bounds)
        return [IntermediateLine(self,
            {
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "color": color,
                "opacity": opacity,
                "width": width
            }),
            *layout_intermediates]

    def get_name(self=None):
        return "line"
    
    def get_args():
        return {
            "allowed": ["x1", "y1", "x2", "y2", "width", "layer", "line_width", "color", "layout"],
            "positional": ["x1", "y1", "x2", "y2", "color"],
            "required": ["x1", "y1", "x2", "y2"]
        }