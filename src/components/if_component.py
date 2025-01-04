from component import Component

class IfComponent(Component):
    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)

    def to_intermediate(self, bounds):
        return self.get_layout_intermediates(bounds)
    
    def read_child_components(self):
        print(self.option("condition"))
        if self.option("condition"):
            return super().read_child_components()
        return []
    
    def get_name(self=None):
        return "if"
    
    def get_args():
        return {
            "allowed": ["condition"],
            "positional": ["condition"],
            "required": ["condition"]
        }