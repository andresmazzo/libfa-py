"""Movie model module"""


class Movie():
    """Movie Class"""
    attributes = ('id', 'name', 'rating')

    def __init__(self, obj):
        self.id = obj.id
        self.name = obj.name
        self.rating = obj.rating

    def get_attributes(self):
        """get attributes"""
        return self.attributes

    def get_all(self):
        """get values"""
        return [self.id, self.name, self.rating]
