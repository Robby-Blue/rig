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
                "height": self.option("height"),
                "width": self.option("width"),
                "xmlns": "http://www.w3.org/2000/svg"
            },
            layout_svg)
    
    def __str__(self):
        bounds = (0, 0, self.option("width"), self.option("height"))
        render_config = (self.option("width"), self.option("height"))
        return str(self.to_svg(bounds, render_config))
    
    def get_name():
        return "svg"