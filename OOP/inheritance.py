class Perent:
    def __init__(self, param_1):
        self.attribute = param_1

    def perent_method(self):
        return self.attribute * 3


class Child(Perent):
    def __init__(self, param_1, param_2):
        super().__init__(param_1)
        self.attribute_child = param_2

    def cheld_method(self):
        return self.attribute_child * 2


parent = Perent("Hi")
child = Child("Hi", "HELLO")
