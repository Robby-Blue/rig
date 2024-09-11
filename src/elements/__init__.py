from elements.root_element import RootElement
from elements.rect_element import RectElement
from elements.circle_element import CircleElement
from elements.text_element import TextElement
from elements.container_element import ContainerElement

types = [
    RootElement,
    RectElement,
    CircleElement,
    TextElement,
    ContainerElement
]

def get_element_contructor(name):
    for e in types:
        if e.get_name() == name:
            return e
    return None