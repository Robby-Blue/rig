class CompileException(Exception):
    def __init__(self, type, pos, message, fix=None):
        self.type = type
        if isinstance(pos, tuple):
            self.start_index, self.end_index = pos
        else:
            self.start_index = pos["start_index"]
            self.end_index = pos["end_index"]
        self.message = message
        self.fix = fix
        super(Exception, self)
