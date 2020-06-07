## Web

Actually [Filmaffinity](https://www.filmaffinity.com/) has only one Web version.

### V1
For more detail see [implementation](/libfa/web/v1/__init__.py).

**Find a movie by id**

https://www.filmaffinity.com/ar/film534365.html
```python
import libfa.web.v1 as fawebv1

movie = fawebv1.movie('ar', '534365')
movie
{
    'id': '534365', 
    'name': 'La zona ', 
    'description': 'En un lugar de Rusia llamado "La Zona", hace algunos años se estrelló un meteorito. A pesar de que el acceso a este lugar está prohibido, los "stalkers" se dedican a guiar a quienes se atreven a aventurarse en este inquietante paraje. (FILMAFFINITY)', 
    'director': {
        'url': 'https://www.filmaffinity.com/ar/search.php?stype=director&sn&stext=Andrei%20Tarkovsky',
        'name': 'Andrei Tarkovsky',
    },
    'actors': [
        {
            'url': '..',
            'name': '..'
        },
        ...
    ],
    'duration': '161 min.', 
    'genre': ['Ciencia ficción', 'Drama'],
    'published_at': '1979',
    'rating': {
        'value': '7.9',
        'best': '10',
        'worst': '1',
        'review_count': '189',
        'rating_count': '12786',
    },
    'reviews': [
        {
            'body': '"Aburrida"',
            'author': 'Carlos Boyero: Diario El Mundo ',
        },
        ...
    ]
}
```

**Get Top Filmaffinity**

https://www.filmaffinity.com/ar/topgen.php
```python
import libfa.web.v1 as fawebv1

results = fawebv1.top_fa('ar', {})
# search by genre
results = fawebv1.top_fa('ar', { 'genre': 'AC'})
# more complex search
params = { 'fromyear': '1978', 'toyear': '1999', 'country': 'AR'}
results = fawebv1.top_fa('ar', params)

results
[
    {
        'id': '1234',
        'title': '..',
        'year': '1999',
        'avg_rating': '9.1',
        'rat_count': '3561'
    },
    ...
]
```

**Best Tops Filmaffinity**

https://www.filmaffinity.com/ar/best_tops.php
```python
import libfa.web as fawebv1

results = fawebv1.best_tops('ar')

results
{
    'menu': {
        'countries': [ ... ],
        'genres': [ ... ]
    },
    'cards': [
        {
            'slug': 'best-all',
            'type': 'country',
            'title': '...',
            'links': [
                {
                    'name': '...',
                    'url': '...',
                },
                ...
            ]
        },
        ...
    ]
}
```

**Global Search**
```python
import libfa.web as fawebv1

results = fawebv1.search('ar', {'stext': 'Stalker'})
# search by title
results = fawebv1.search('ar', {'stext': 'Stalker', 'stype': 'title'})
# search by cast
results = fawebv1.search('ar', {'stext': 'James Stewart', 'stype': 'cast'})
# search by director
results = fawebv1.search('ar', {'stext': 'Francis Ford Coppola', 'stype': 'director'})
results
[
    {
        'id': '1234',
        'title': '..',
        'director': '...'
    },
    ...
]
```