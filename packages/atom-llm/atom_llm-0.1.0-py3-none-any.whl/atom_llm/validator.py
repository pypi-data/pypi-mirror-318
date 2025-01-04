class Validator:
    def validate(self, value):
        raise NotImplementedError

class EqualValidator(Validator):
    pass