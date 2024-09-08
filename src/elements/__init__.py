from elements.svg_root_element import SVGRootElement
from elements.rect_element import RectElement
from elements.text_element import TextElement
from elements.container_element import ContainerElement

types = [
    SVGRootElement,
    RectElement,
    TextElement,
    ContainerElement
]

def get_element_contructor(name):
    for e in types:
        if e.get_name() == name:
            return e
    return None