from svg_writer import SVGElement

class SVGCircleElement(SVGElement):

    def __init__(self, attributes, children=None):
        super().__init__("circle", attributes, children)

    def render(self, img):
        # TODO this supports outline too 
        x = self.get("cx")
        y = self.get("cy")
        img.circle((x, y),
            radius=self.get("r"),
            fill=self.get("fill"))