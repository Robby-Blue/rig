from layout import Layout

class HListLayout(Layout):
    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)
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
        
        space = self.option("space", "fill")

        width_left = (x2-x1)-total_width

        default_width = 0
        if space == "fill" and unset_components >= 1:
            default_width = width_left / unset_components

        children = []

        for child in self.parent.children:
            child_y1, child_y2 = self.calc_pos_in_bounds(child.option("y", 0), child.get_height(bounds), y1, y2)

            if child.has_option("width"):
                width = percent_width * child.get_width(bounds)
            else:
                width = default_width
            child_bounds = (pos_x, child_y1, pos_x+width, child_y2)
            children += child.to_intermediate(child_bounds)

            pos_x += width
            if space == "space_between":
                pos_x += width_left / (len(self.parent.children) - 1)

        return children
    
    def get_name(self=None):
        return "hlist"
    
    def get_args():
        return {
            "allowed": ["space"],
            "positional": [],
            "required": []
        }