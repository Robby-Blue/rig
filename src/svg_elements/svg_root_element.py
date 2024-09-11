from svg_writer import SVGElement

class SVGRootElement(SVGElement):

    def __init__(self, attributes, children=None):
        super().__init__("svg", attributes, children)

    def render(self, img):
        pass