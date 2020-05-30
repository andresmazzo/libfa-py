from tinydb import TinyDB, Query

dbs = {}
# Movies
# attributes = ('id', 'name', 'rating')
dbs['movies'] = TinyDB('temp/db/movies.json')

# Lists
# attributes = ('id', 'name')
dbs['lists'] = TinyDB('temp/db/lists.json')


def get_db(name):
    return dbs[name]
