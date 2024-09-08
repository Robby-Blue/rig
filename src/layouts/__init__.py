from layouts.v_list_layout import VListLayout
from layouts.h_list_layout import HListLayout
from layouts.relative_layout import RelativeLayout

types = [
    VListLayout,
    HListLayout,
    RelativeLayout
]

def get_layout_contructor(name):
    for e in types:
        if e.get_name() == name:
            return e
    return None