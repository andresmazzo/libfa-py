"""List model module"""


class List():
    """List Class"""
    attributes = ('id', 'name')

    def __init__(self, obj):
        self.id = obj['id']
        self.name = obj['name']

    def get_attributes(self):
        """get attributes"""
        return self.attributes

    def get_all(self):
        """get values"""
        return [self.id, self.name]
