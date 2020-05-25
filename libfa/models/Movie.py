"""Movie model module"""


class Movie():
    """Movie Class"""
    attributes = ('id', 'name', 'rating')

    def _init(self, obj):
        self.attributes = obj

    def get_attrs(self):
        """get attributes"""
        return self.attributes

    def set_attr(self, attr, val):
        """set an specified attribute"""
        self.attributes[attr] = val
