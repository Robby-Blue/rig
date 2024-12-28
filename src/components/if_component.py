from component import Component

class IfComponent(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_intermediate(self, bounds):
        if self.option("condition"):
            layout_intermediates = self.get_layout_intermediates(bounds)
            return layout_intermediates
        return []
    
    def get_name(self=None):
        return "if"
    
    def get_args():
        return {
            "allowed": ["condition"],
            "positional": ["condition"],
            "required": ["condition"]
        }