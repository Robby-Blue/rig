class BadSyntaxException(Exception):
    def __init__(self, start_index, end_index, message, fix=None):
        self.start_index = start_index
        self.end_index = end_index
        self.message = message
        self.fix = fix
        super(Exception, self)
