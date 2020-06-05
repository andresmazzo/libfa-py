## Web

### Drivers
#### V1
Actually [Filmaffinity](https://www.filmaffinity.com/) has only one Web version.

For more detail see [implementation](/libfa/web/v1/__init__.py).

### Examples

**Find a movie by id**
```python
import libfa.web.v1 as fawebv1

movie = fawebv1.movie('ar', 1234)

movie['id']
1234
movie['name']
Stalker
movie['description']
Some cool description...
movie['genre']
Drama
```

**Get Top Filmaffinity**
https://www.filmaffinity.com/ar/topgen.php
```python
import libfa.web.v1 as fawebv1

results = fawebv1.top_fa('ar')
```

**Best Tops Filmaffinity**
https://www.filmaffinity.com/ar/best_tops.php
```python
import libfa.web as fawebv1

results = fawebv1.best_tops('ar')
```

**Find a movie by id**
```python
import libfa.web as fawebv1

results = fawebv1.search('ar', 'Stalker')
```