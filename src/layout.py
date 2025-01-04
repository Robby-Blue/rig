from component import Component

class Layout(Component):

    parent = None

    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)
        
    def set_parent(self, parent):
        self.parent = parent

    def get_args():
        return None