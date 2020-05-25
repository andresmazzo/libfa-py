"""csv_v1 ratings module."""

import csv


def lists(data, filepath):
    """generate ratings file."""
    fp = open(filepath, 'w')
    writer = csv.writer(fp)

    writer.writeRow(header())

    for item in data:
        writer.writerow([item.id, item.name])


def header():
    """get header."""
    return [
        'ID',
        'Name'
    ]
