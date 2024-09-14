from svg_writer import SVGElement

class SVGLineElement(SVGElement):

    def __init__(self, src, attributes, children=None):
        super().__init__("line", src, attributes, children)

    def render(self, img):
        x1 = self.get("x1")
        y1 = self.get("y1")
        x2 = self.get("x2")
        y2 = self.get("y2")

        img.line((x1, y1, x2+1, y2+1),
            fill=self.get("stroke"),
            width=int(self.get("stroke-width")))