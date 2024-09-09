from element import Element
from svg_writer import SVGElement

class RectElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = self.option("color", "black")
        self.opacity = self.option("opacity", 1)

    def to_svg(self, bounds, render_config):
        border_radius = render_config[0] * 0.02

        margin_bounds = self.get_margin_bounds(bounds, render_config)
        x1, y1, x2, y2 = margin_bounds

        width = x2-x1
        height = y2-y1

        layout_svg = self.get_layout_svg(margin_bounds, render_config)
        return [SVGElement(
            "rect",
            {
                "x": x1,
                "y": y1,
                "width": width,
                "height": height,
                "rx": border_radius,
                "ry": border_radius,
                "fill": self.color,
                "fill-opacity": self.opacity
            }),
            *layout_svg]
    
    def get_name():
        return "rect"