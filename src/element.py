class Element():

    options = {}

    def __init__(self, **kwargs):
        self.options = kwargs

        self.layout = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def set_layout(self, layout):
        layout.set_parent(self)
        self.layout = layout

    def get_layout_svg(self, bounds, render_config):
        if not self.children:
            return []
        if not self.layout:
            from layouts import VListLayout
            self.set_layout(VListLayout())
        return self.layout.to_svg(bounds, render_config)

    def to_svg(bounds, render_config):
        return []

    def get_margin_bounds(self, bounds, render_config):
        margin = render_config[0] * 0.003

        x1, y1, x2, y2 = bounds

        x1+=margin
        y1+=margin
        x2-=margin
        y2-=margin

        return (x1, y1, x2, y2)
    
    def option(self, key, default=None):
        if not key in self.options:
            if default is not None:
                return default
            else:
                print(self.__class__.__name__, "doesnt have", key)
                return None
        return self.options[key]
    
    def has_option(self, key):
        return key in self.options