from layout import Layout

class HListLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # whether and how theres lines between the elements like borders

    def to_svg(self, bounds, render_config):
        x1, y1, x2, y2 = bounds
        percent_width = (x2-x1) / 100

        pos_x = x1

        total_width = 0
        unset_elements = 0
        for child in self.parent.children:
            if child.has_option("width"):
                total_width += percent_width * child.option("width")
            else:
                unset_elements += 1
        
        width_left = (x2-x1)-total_width

        svg_children = []

        for child in self.parent.children:
            if child.has_option("width"):
                width = percent_width * child.option("width")
            else:
                width = width_left / unset_elements
            child_bounds = (pos_x, y1, pos_x+width, y2)
            svg_children += child.to_svg(child_bounds, render_config)

            pos_x+=width

        return svg_children
    
    def get_name():
        return "hlist"