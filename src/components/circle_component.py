from component import Component
from intermediates import IntermediateCircle

from utils import hex_rgba_to_rgba_alpha

class CircleComponent(Component):
    def __init__(self, **kwargs):
        if "size" in kwargs:
            kwargs["width"] = kwargs["size"]
            kwargs["height"] = kwargs["size"]
        super().__init__(**kwargs)

    def to_intermediate(self, bounds):
        margin_bounds = self.get_margin_bounds(bounds)
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
        
        fill_color, fill_opacity = hex_rgba_to_rgba_alpha(self.option("fill_color", "#00000000"))
        stroke_color, stroke_opacity = hex_rgba_to_rgba_alpha(self.option("color", "#FFFFFF"))

        layout_intermediates = self.get_layout_intermediates(margin_bounds)

        return [IntermediateCircle(self,
            {
                "x": x,
                "y": y,
                "radius": size,
                "fill-color": fill_color,
                "fill-opacity": fill_opacity,
                "stroke-color": stroke_color,
                "stroke-width": self.root().option("width")/300,
                "stroke-opacity": stroke_opacity
            }),
            *layout_intermediates]
    
    def get_orientation(self, bounds):
        if self.option("size_type", "") == "rel_abs":
            return "h"
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
        return "h"

    def get_size(self, bounds):
        bounds = self.get_margin_bounds(bounds)
        x1, y1, x2, y2 = bounds
        orientation = self.get_orientation((x1, y1, x2, y2))

        total_width = (x2-x1)
        total_height = (y2-y1)

        size_type = self.option("size_type", "rel_parent")

        if orientation == "h":
            percent_width = self.option("width")
            width = total_width * percent_width

            percent_height = width / total_height
            if size_type == "rel_abs":
                percent_width *= self.root().option("width") / total_width
        elif orientation == "v":
            percent_height = self.option("height")
            height = total_height * percent_height

            percent_width = height / total_width
            if size_type == "rel_abs":
                percent_height *= self.root().option("height") / total_height

        return [percent_width, percent_height]

    def get_name(self=None):
        return "circle"
    
    def get_args():
        return {
            "allowed": ["x", "y", "layer", "layout", "fill_color", "color", "width", "size_type", "orientation", "size", "height"],
            "positional": ["x", "y", "size", "color"],
            "required": []
        }