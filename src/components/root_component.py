from component import Component
from svg_elements import SVGRootElement

class RootComponent(Component):
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
    
    def get_args():
        return {
            "allowed": ["width", "height", "layout"],
            "positional": ["width", "height"],
            "required": []
        }