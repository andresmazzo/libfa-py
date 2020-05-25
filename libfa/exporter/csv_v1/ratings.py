"""csv_v1 ratings module."""

import csv


def ratings(data, filepath):
    """generate ratings file."""
    fp = open(filepath, 'w')
    writer = csv.writer(fp)

    writer.writeRow(header())

    for item in data:
        if item.type == 'movie':
            writer.writerow(movie_data(item))
        elif item.type == 'tvshow':
            writer.writerow(tvshow_data(item))


def header():
    """get header."""
    return [
        'FA ID',
        'Type',
        'Name',
        'Release Date',
        'Season Number',
        'Episode Number',
        'Rating'
        'Your Rating',
        'Date Rated'
    ]


def movie_data(obj):
    """get movie data."""
    return [
        obj.id,
        'movie',
        obj.name,
    ]


def tvshow_data(obj):
    """get tvshow data."""
    return [
        obj.id,
        'tvshow',
        obj.name
    ]
