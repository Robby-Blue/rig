from element import Element

class ContainerElement(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_svg(self, bounds, render_config):
        layout_svg = self.get_layout_svg(bounds, render_config)
        return layout_svg
    
    def get_name():
        return "container"