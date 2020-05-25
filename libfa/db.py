"""This module acts as a database layer."""


class DB:
    """DB class is the api for this layer."""

    def __init__(self, name):
        self.name = name
        self.init_db()

    def init_db(self):
        """Initialize database."""
        self.data = {}
        self.data['user'] = {}  # account, friends, lists, ratings, etc
        self.data['medias'] = {}  # movies and tv shows

    def get(self, key):
        """Get an specified data."""
        return self.data[key]

    def insert(self, key, data):
        """Insert some data on specified key."""
        self.data[key] = data
