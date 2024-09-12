from element import Element
from svg_elements import SVGRootElement

class RootElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_svg(self, bounds=None):
        bounds = (0, 0, self.get_width(), self.get_height())
        
        layout_svg = self.get_layout_svg(bounds)

        return SVGRootElement(self,
            {
                "height": self.get_height(),
                "width": self.get_width(),
                "xmlns": "http://www.w3.org/2000/svg"
            },
            layout_svg)
    
    def __str__(self):
        return str(self.to_svg())
    
    def get_name(self=None):
        return "svg"