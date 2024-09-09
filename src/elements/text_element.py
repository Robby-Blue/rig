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
        
        align_h = "right"
        if self.option("center_h", False) == True:
            align_h = "center"
        if self.has_option("align_text_h"):
            align_h = self.option("align_text_h", "")

        align_v = "bottom"
        if self.option("center_v", False) == True:
            align_v = "center"
        if self.has_option("align_text_v"):
            align_v = self.option("align_text_v", "")

        text_anchor = "middle"
        dy = "0.25em"
        # normally youd use dominant-baseline,
        # but that doesnt work everywhere

        if align_h == "right":
            x1, _, _, _ = self.get_margin_bounds(bounds, render_config)
            text_anchor = "start"
        if align_h == "left":
            text_anchor = "end"
        if align_v == "bottom":
            _, y1, _, _ = self.get_margin_bounds(bounds, render_config)
            dy = "1em"

        svg_element = SVGElement(
            "text",
            {
                "x": x1,
                "y": y1,
                "text-anchor": text_anchor,
                "dy": dy,
                "fill": self.color,
                "fill-opacity": self.opacity
            },
            [self.text])

        return [svg_element]
    
    def get_name():
        return "text"