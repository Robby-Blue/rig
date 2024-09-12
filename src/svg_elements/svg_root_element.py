from svg_writer import SVGElement

class SVGRootElement(SVGElement):

    def __init__(self, src, attributes, children=None):
        super().__init__("svg", src, attributes, children)

    def render(self, img):
        pass