from element import Element
from svg_elements import SVGLineElement

from utils import hex_rgba_to_rgba_alpha

class LineElement(Element):
    def __init__(self, **kwargs):
        if "width" in kwargs:
            kwargs["line_width"] = kwargs["width"]

        kwargs["x"] = kwargs["x1"]
        kwargs["y"] = kwargs["y1"]
        kwargs["width"] = kwargs["x2"] - kwargs["x1"]
        kwargs["height"] = kwargs["y2"] - kwargs["y1"]

        super().__init__(**kwargs)

    def to_svg(self, bounds):
        base_width = self.root().option("width") * 0.005
        width = self.option("line_width", 1) * base_width

        x1, y1, x2, y2 = bounds

        color, opacity = hex_rgba_to_rgba_alpha(self.option("color", "#FFFFFF"))

        layout_svg = self.get_layout_svg(bounds)
        return [SVGLineElement(self,
            {
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "stroke": color,
                "stroke-opacity": opacity,
                "stroke-width": width
            }),
            *layout_svg]

    def get_name(self=None):
        return "line"