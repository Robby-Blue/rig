from layout import Layout

class RelativeLayout(Layout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_intermediate(self, bounds):
        x1, y1, x2, y2 = bounds

        children = []

        for child in self.parent.children:
            pos_percent_width = (x2-x1) / 100 * (100-child.get_width(bounds))
            pos_percent_height = (y2-y1) / 100 * (100-child.get_height(bounds))

            percent_width = (x2-x1) / 100
            percent_height = (y2-y1) / 100

            dx = pos_percent_width * child.option("x", 0) / 100
            dy = pos_percent_height * child.option("y", 0) / 100
            
            width = percent_width * child.get_width(bounds)
            height = percent_height * child.get_height(bounds)

            dx = self.align(dx, width, percent_width, "h", child)
            dy = self.align(dy, height, percent_height, "v", child)

            child_bounds = (x1+dx, y1+dy, x1+dx+width, y1+dy+height)
            children += child.to_intermediate(child_bounds)

        return children
    
    def align(self, pos, length, percent_length, direction, child):
        expected_align_h = ""
        if child.option(f"center_{direction}", False):
            pos = 50 * percent_length
            expected_align_h = "center"

        align_h = child.option(f"align_{direction}", expected_align_h)
        if align_h == "center":
            pos -= length/2
        if align_h == "right":
            pos -= length

        return pos
    
    def get_name(self=None):
        return "relative"
    
    def get_args():
        return {
            "allowed": [],
            "positional": [],
            "required": []
        }