from component import Component

class RootComponent(Component):
    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)

    def to_intermediate(self, bounds=None):
        bounds = (0, 0, self.get_width(), self.get_height())
        
        layout_intermediates = self.get_layout_intermediates(bounds)

        return {
            "width": self.get_width(),
            "height": self.get_height(),
            "children": layout_intermediates
        }
    
    def __str__(self):
        return str(self.to_intermediate())
    
    def get_name(self=None):
        return "svg"
    
    def get_args():
        return {
            "allowed": ["width", "height", "layout"],
            "positional": ["width", "height"],
            "required": []
        }