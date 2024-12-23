from component import Component

class Layout(Component):

    parent = None

    def __init__(self, **kwargs):
        pass

    def set_parent(self, parent):
        self.parent = parent

    def get_args():
        return None