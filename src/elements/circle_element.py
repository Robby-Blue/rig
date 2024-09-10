from element import Element
from svg_writer import SVGElement

class CircleElement(Element):
    def __init__(self, **kwargs):
        if "size" in kwargs:
            kwargs["width"] = kwargs["size"]
            kwargs["height"] = kwargs["size"]
        super().__init__(**kwargs)

    def to_svg(self, bounds, render_config):
        margin_bounds = self.get_margin_bounds(bounds, render_config)
        x1, y1, x2, y2 = margin_bounds

        orientation = self.get_orientation((x1, y1, x2, y2))

        if orientation == "h":
            size = (x2-x1) / 2
        elif orientation == "v":
            size = (y2-y1) / 2
        else:
            # TODO add some actual errors
            return
        
        x = (x1+x2)/2
        y = (y1+y2)/2
        
        layout_svg = self.get_layout_svg(margin_bounds, render_config)
        return [SVGElement(
            "circle",
            {
                "r": size,
                "cx": x,
                "cy": y,
                "fill": self.option("color", "black"),
                "opacity": self.option("opacity", 1)
            }),
            *layout_svg]
    
    def get_orientation(self, bounds):
        if self.option("orientation", "") == "h":
            return "h"
        if self.option("orientation", "") == "v":
            return "v"
        if self.has_option("size"):
            x1, y1, x2, y2 = bounds
            dx = x2 - x1
            dy = y2 - y1
            return "v" if dx > dy else "h"
        if self.parent:
            parent_layout = self.parent.layout.get_name()
            if parent_layout == "hlist":
                return "h"
            if parent_layout == "vlist":
                return "v"
        if self.has_option("width"):
            return "h"
        if self.has_option("height"):
            return "v"
        return None

    def get_size(self, bounds):
        x1, y1, x2, y2 = bounds
        orientation = self.get_orientation((x1, y1, x2, y2))

        print(orientation)
        if orientation == "h":
            total_width = (x2-x1)
            percent_width = self.option("width")
            width = total_width * percent_width

            total_height = (y2-y1)
            percent_height = width / total_height
            return [percent_width, percent_height]
        elif orientation == "v":
            total_height = (y2-y1)
            percent_height = self.option("height")
            height = total_height * percent_height

            total_width = (x2-x1)
            percent_width = height / total_width
            return [percent_width, percent_height]

    def get_name(self=None):
        return "circle"