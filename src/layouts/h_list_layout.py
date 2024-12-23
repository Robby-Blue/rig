from layout import Layout

class HListLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # whether and how theres lines between the components like borders

    def to_intermediate(self, bounds):
        x1, y1, x2, y2 = bounds
        percent_width = (x2-x1) / 100

        pos_x = x1

        total_width = 0
        unset_components = 0
        for child in self.parent.children:
            if child.has_option("width"):
                total_width += percent_width * child.option("width")
            else:
                unset_components += 1
        
        width_left = (x2-x1)-total_width

        children = []

        for child in self.parent.children:
            if child.has_option("width"):
                width = percent_width * child.get_width(bounds)
            else:
                width = width_left / unset_components
            child_bounds = (pos_x, y1, pos_x+width, y2)
            children += child.to_intermediate(child_bounds)

            pos_x+=width

        return children
    
    def get_name(self=None):
        return "hlist"
    
    def get_args():
        return {
            "allowed": [],
            "positional": [],
            "required": []
        }