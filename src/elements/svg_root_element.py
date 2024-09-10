from element import Element
from svg_writer import SVGElement

class SVGRootElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_svg(self, bounds, render_config):
        layout_svg = self.get_layout_svg(bounds, render_config)

        return SVGElement(
            "svg",
            {
                "height": self.get_height(),
                "width": self.get_width(),
                "xmlns": "http://www.w3.org/2000/svg"
            },
            layout_svg)
    
    def __str__(self):
        bounds = (0, 0, self.get_width(), self.get_height())
        render_config = (self.get_width(), self.get_height())
        return str(self.to_svg(bounds, render_config))
    
    def get_name(self=None):
        return "svg"