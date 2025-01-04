from component import Component

class ContainerComponent(Component):
    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)

    def to_intermediate(self, bounds):
        layout_intermediates = self.get_layout_intermediates(bounds)
        return layout_intermediates
    
    def get_name(self=None):
        return "container"
    
    def get_args():
        return {
            "allowed": ["x", "y", "layer", "width", "height", "layout"],
            "positional": ["x", "y", "width", "height"],
            "required": []
        }