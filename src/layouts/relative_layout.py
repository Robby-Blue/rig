from layout import Layout

class RelativeLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_svg(self, bounds, render_config):
        x1, y1, x2, y2 = bounds
        percent_width = (x2-x1) / 100
        percent_height = (y2-y1) / 100

        svg_children = []

        for child in self.parent.children:
            dx = percent_width * child.option("x", 0)
            dy = percent_height * child.option("y", 0)
            
            child_bounds = (x1+dx, y1+dy, 0, 0)
            svg_children += child.to_svg(child_bounds, render_config)

        return svg_children
    
    def get_name():
        return "relative"