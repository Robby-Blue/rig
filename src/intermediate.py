class IntermediateElement():

    def __init__(self, src, kwargs):
        self.src = src
        self.attributes = kwargs

    def get(self, key):
        return self.attributes[key]

    def to_svg(self):
        raise NotImplementedError()
    
    def draw(self):
        raise NotImplementedError()