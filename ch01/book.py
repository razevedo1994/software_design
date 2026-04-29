class Book:
    def __init__(self, attributes):
        self._attributes = attributes

    @property
    def attributes(self):
        return self.attributes
