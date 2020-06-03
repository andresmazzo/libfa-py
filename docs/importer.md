## Importer

### Drivers
#### User Exportdata
Filmaffinity export method actually is very poor. After you request data, it would send you an email with a `.zip file`. Inside it you find an old html webpage. 
You could open `index.html` and navigate. But, what if you need your data processable, or useful for other software systems (IMDB, TMDB, etc)? You can't.
Here comes **libfa** to rescue! :tada:

We provide an importer that reads the html and in some views, use Microdata.

### Examples

```python
import libfa.importer as faimporter

faimporter.exportdata.support()
['index', 'account-data', 'movie-ratings', 'lists', 'friend-groups']

data = faimporter.exportdata.run('/your/path/file.zip')
data['pages']
data['sections']
```