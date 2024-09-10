from element import Element
from svg_writer import SVGElement

class CircleElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # TODO: lots of fixing with width and height
    # dont just get the values, instead get them by method
    # which can then calculate with orientation and stuff

    def to_svg(self, bounds, render_config):
        margin_bounds = self.get_margin_bounds(bounds, render_config)
        x1, y1, x2, y2 = margin_bounds

        orientation = self.get_orientation()

        if orientation == "h":
            size = (x2-x1) / 2
        elif orientation == "v":
            size = (y2-y1) / 2
        else:
            # TODO add some actual errors
            return
        
        x1 += size
        y1 += size

        layout_svg = self.get_layout_svg(margin_bounds, render_config)
        return [SVGElement(
            "circle",
            {
                "r": size,
                "cx": x1,
                "cy": y1,
                "fill": self.option("color", "black"),
                "opacity": self.option("opacity", 1)
            }),
            *layout_svg]
    
    def get_orientation(self):
        if self.has_option("width"):
            return "h"
        if self.option("orientation", "") == "h":
            return "h"
        if self.has_option("height"):
            return "v"
        if self.option("orientation", "") == "v":
            return "v"
        if self.parent:
            parent_layout = self.parent.layout.get_name()
            if parent_layout == "hlist":
                return "h"
            if parent_layout == "vlist":
                return "v"

        return None

    def get_name(self=None):
        return "circle"