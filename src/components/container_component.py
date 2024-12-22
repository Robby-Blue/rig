from component import Component

class ContainerComponent(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_svg(self, bounds):
        layout_svg = self.get_layout_svg(bounds)
        return layout_svg
    
    def get_name(self=None):
        return "container"
    
    def get_args():
        return {
            "allowed": ["x", "y", "layer", "width", "height", "layout"],
            "positional": ["x", "y", "width", "height"],
            "required": []
        }