
class Generics:

    def __init__(self, *args, **kwargs):
        pass

    def data(self, value):
        self.value = {'type': type(value)}


class Validator:
    
    def __init__(self):
        pass

    def validate(self):
        pass

class PredictValidator:
    
    def __init__(self, name, length):
        self.rules = [
                {
                    'variable': name,
                    'type': list(),
                    'length': int(length)
                }
            ]
