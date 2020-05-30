"""csv_v1 ratings module."""

import csv
from libfa.models.ListModel import List as ListModel
from typing import List


def lists(data: List, filepath: str):
    """generate ratings file."""
    fp = open(filepath, 'w')
    writer = csv.writer(fp)

    writer.writerow(header())

    for item in data:
        writer.writerow([item.id, item.name])


def header():
    """get header."""
    return [
        'ID',
        'Name'
    ]
