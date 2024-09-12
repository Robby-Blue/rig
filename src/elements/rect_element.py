from element import Element
from svg_elements import SVGRectElement

class RectElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_svg(self, bounds, render_config):
        border_radius = render_config[0] * 0.02

        margin_bounds = self.get_margin_bounds(bounds, render_config)
        x1, y1, x2, y2 = margin_bounds

        width = x2-x1
        height = y2-y1

        inner_padding = self.option("inner_padding", 0)
        layout_bounds = self.get_margin_bounds(margin_bounds, render_config, inner_padding)

        layout_svg = self.get_layout_svg(layout_bounds, render_config)
        return [SVGRectElement(self,
            {
                "x": x1,
                "y": y1,
                "width": width,
                "height": height,
                "rx": border_radius,
                "ry": border_radius,
                "fill": self.option("color", "#00000000"),
                "stroke": self.option("stroke", "#FFFFFF"),
                "stroke-width": 2
            }),
            *layout_svg]
    
    def get_name(self=None):
        return "rect"