from svg_writer import SVGElement

class SVGRectElement(SVGElement):

    def __init__(self, src, attributes, children=None):
        super().__init__("rect", src, attributes, children)

    def render(self, img):
        x1 = self.get("x")
        y1 = self.get("y")
        x2 = x1 + self.get("width")
        y2 = y1 + self.get("height")
        img.rounded_rectangle((x1, y1, x2, y2),
            fill=self.get("fill"),
            outline=self.get("stroke"),
            width=self.get("stroke-width"),
            radius=self.get("rx"))