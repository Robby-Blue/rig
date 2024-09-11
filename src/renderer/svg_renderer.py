from svg_writer import SVGElement
from PIL import Image, ImageDraw

def render(svg):
    img = Image.new(mode="RGBA", size=(svg.get("width"), svg.get("height")))
    draw = ImageDraw.Draw(img)

    render_element(svg, draw)
    
    return img

def render_element(element, img):
    element.render(img)
    for child in element.children:
        if not isinstance(child, SVGElement):
            continue
        render_element(child, img)