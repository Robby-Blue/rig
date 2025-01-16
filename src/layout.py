from component import Component

class Layout(Component):

    parent = None

    def __init__(self, src, variables, templates):
        super().__init__(src, variables, templates)
    
    def calc_pos_in_bounds(self, child_pos_percent, length, p1, p2):
        pos_percent_width = (p2-p1) / 100 * (100-length)

        percent_width = (p2-p1) / 100

        child_pos = p1 + pos_percent_width * child_pos_percent / 100
        child_length = percent_width * length

        return (child_pos, child_pos + child_length)

    def set_parent(self, parent):
        self.parent = parent

    def get_args():
        return None