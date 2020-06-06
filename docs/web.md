## Web

Actually [Filmaffinity](https://www.filmaffinity.com/) has only one Web version.

### V1
For more detail see [implementation](/libfa/web/v1/__init__.py).

**Find a movie by id**

https://www.filmaffinity.com/ar/film534365.html
```python
import libfa.web.v1 as fawebv1

movie = fawebv1.movie('ar', 534365)

movie['id']
534365
movie['name']
Stalker
movie['description']
En un lugar de...
movie['genre']
['Ciencia Ficción', 'Drama', ...]
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