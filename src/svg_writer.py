from html import escape

class SVGElement():

    def __init__(self, tag, attributes, children=None):
        self.tag = tag

        self.attributes = attributes
        if not isinstance(children, list):
            children = [children]

        self.children = children

    def render(self, img):
        pass

    def get(self, key):
        return self.attributes[key]

    def __str__(self):
        attributes_str = ""
        for key, val in self.attributes.items():
            key = escape(key)

            if isinstance(val, dict):
                if not val["set"]:
                    continue
                val = val["value"]

            val = escape(str(val))
            attributes_str += f" {key}=\"{val}\""
        
        inner = ""
        for child in self.children:
            if child is None:
                continue
            inner += str(child)

        if not len(self.children):
            return f"<{self.tag}{attributes_str} />"
        else:
            return f"<{self.tag}{attributes_str}>{inner}</{self.tag}>"

def svg(attrs, children=None):
    return SVGElement("svg", attrs, children)