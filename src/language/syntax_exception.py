class BadSyntaxException(Exception):
    def __init__(self, position, message):
        self.position = position
        self.message = message 
        super(Exception, self)
