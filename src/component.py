import expressions

class Component():

    def __init__(self, src, variables, templates):
        self.children = []
        self.parent = None

        self.options = dict(src)
        self.variables = variables
        self.templates = templates

        self.variables = variables
        self.variables = expressions.precalculate_vars(self.variables, variables)
        self.options = expressions.precalculate_vars(self.options, self.variables)

        if "children" in self.options:
            self.read_layout()
            self.read_child_components()

        self.layer = self.option("layer", 0)

    def read_layout(self):
        src_layout = self.option("layout", {"type": "relative"})
        layout_type_name = src_layout["type"]
        from layouts import get_layout_contructor
        layout_type = get_layout_contructor(layout_type_name)

        layout = layout_type(src_layout, self.variables, {})

        self.set_layout(layout)

    def read_child_components(self):
        for child in self.options["children"]:
            component = Component.read_child_component(child, self.variables, self.templates)
            self.add_child(component)

    def read_child_component(component, variables, templates):
        from components import get_component_contructor
        component_type_name = component["type"]

        if component_type_name == "template":
            template_name = component["name"]
            template = dict(templates[template_name])
            component = expressions.precalculate_vars(component, variables)
            return Component.read_child_component(template, component, templates)
        else:
            component_type = get_component_contructor(component_type_name)
            component = component_type(component, variables, templates)
            return component

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)
        child.set_parent(self)

    def set_layout(self, layout):
        layout.set_parent(self)
        self.layout = layout

    def get_layout_intermediates(self, bounds):
        if not self.children:
            return []
        if not self.layout:
            from layouts import VListLayout
            self.set_layout(VListLayout())
        return self.layout.to_intermediate(bounds)

    def to_intermediate(bounds):
        return []

    def get_margin_bounds(self, bounds, amplifier=1):
        # TODO: test this more, try a layout flag instead
        margin = self.parent.option("width", 0) * 0.003 * amplifier

        x1, y1, x2, y2 = bounds

        x1+=margin
        y1+=margin
        x2-=margin
        y2-=margin

        return (x1, y1, x2, y2)
    
    def root(self):
        if self.parent:
            return self.parent.root()
        return self
    
    def get_size(self, bounds=None):
        return [self.option("width", 100), self.option("height", 100)]

    def get_width(self, bounds=None):
        return self.get_size(bounds)[0]

    def get_height(self, bounds=None):
        return self.get_size(bounds)[1]
    
    def option(self, key, default=None):
        if not key in self.options:
            if default is not None:
                return default
            else:
                print(self.__class__.__name__, "doesnt have", key)
                return None
        
        return self.options[key]

    def has_option(self, key):
        return key in self.options
    
    def get_args():
        return None