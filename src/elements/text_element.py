from element import Element
from svg_writer import SVGElement

class TextElement(Element):
    def __init__(self, **kwargs):
        kwargs["height"] = 0
        kwargs["width"] = 0
        super().__init__(**kwargs)
        self.text = self.option("text")
        self.color = self.option("color", "black")
        self.opacity = self.option("opacity", 1)

    def to_svg(self, bounds, render_config):
        x1, y1, _, _ = bounds

        svg_element = SVGElement(
            "text",
            {
                "x": x1,
                "y": y1,
                "text-anchor": "middle",
                "dy": "0.25em",
                # normally youd use dominant-baseline,
                # but that doesnt work everywhere
                "fill": self.color,
                "fill-opacity": self.opacity
            },
            [self.text])

        return [svg_element]
    
    def get_name():
        return "text"