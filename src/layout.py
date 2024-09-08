from element import Element

class Layout(Element):

    parent = None

    def __init__(self, **kwargs):
        pass

    def set_parent(self, parent):
        self.parent = parent