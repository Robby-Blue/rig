from component import Component
from intermediates import IntermediateLine

class LineComponent(Component):
    def __init__(self, src, variables, templates):
        if "width" in src:
            src["line_width"] = src["width"]

        src["x"] = src["x1"]
        src["y"] = src["y1"]
        src["width"] = src["x2"] - src["x1"]
        src["height"] = src["y2"] - src["y1"]

        super().__init__(src, variables, templates)

    def to_intermediate(self, bounds):
        base_width = self.root().option("width") * 0.005
        width = self.option("line_width", 1) * base_width

        x1, y1, x2, y2 = bounds

        layout_intermediates = self.get_layout_intermediates(bounds)
        return [IntermediateLine(self,
            {
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "color": self.option("color", 0xFFFFFFFF),
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