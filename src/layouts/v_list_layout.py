from layout import Layout

class VListLayout(Layout):
    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)
        # whether and how theres lines between the components like borders

    def to_intermediate(self, bounds):
        x1, y1, x2, y2 = bounds
        percent_height = (y2-y1) / 100

        pos_y = y1

        total_height = 0
        unset_components = 0
        for child in self.parent.children:
            if child.has_option("height"):
                total_height += percent_height * child.get_height(bounds)
            else:
                unset_components += 1
        
        height_left = (y2-y1)-total_height

        children = []

        for child in self.parent.children:
            if child.has_option("height"):
                height = percent_height * child.get_height(bounds)
            else:
                height = height_left / unset_components
            child_bounds = (x1, pos_y, x2, pos_y+height)
            children += child.to_intermediate(child_bounds)

            pos_y+=height

        return children
    
    def get_name(self=None):
        return "vlist"
    
    def get_args():
        return {
            "allowed": [],
            "positional": [],
            "required": []
        }