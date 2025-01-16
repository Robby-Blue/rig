from layout import Layout

class RelativeLayout(Layout):
    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)

    def to_intermediate(self, bounds):
        x1, y1, x2, y2 = bounds

        children = []

        for child in self.parent.children:
            child_x1, child_x2 = self.calc_pos_in_bounds(child.option("x", 0), child.get_width(bounds), x1, x2)
            child_y1, child_y2 = self.calc_pos_in_bounds(child.option("y", 0), child.get_height(bounds), y1, y2)

            child_bounds = (child_x1, child_y1, child_x2, child_y2)
            children += child.to_intermediate(child_bounds)

        return children
    
    def get_name(self=None):
        return "relative"
    
    def get_args():
        return {
            "allowed": [],
            "positional": [],
            "required": []
        }