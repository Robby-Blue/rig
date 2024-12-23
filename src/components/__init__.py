from components.root_component import RootComponent
from components.rect_component import RectComponent
from components.circle_component import CircleComponent
from components.text_component import TextComponent
from components.line_component import LineComponent
from components.container_component import ContainerComponent

types = [
    RootComponent,
    RectComponent,
    CircleComponent,
    TextComponent,
    LineComponent,
    ContainerComponent
]

def get_component_contructor(name):
    for e in types:
        if e.get_name() == name:
            return e
    return None