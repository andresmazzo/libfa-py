## Introduction
Welcome to the FilmAffinity Python Library. My mission is to rescue from the incompatible protocols and formats the platform has :/.

## Requirements
- Python3
- Python3 BeautifulSoup4 (`sudo pip install BeautifulSoup4` :P)

## Description
Do you want to convert the zip with html old files that FilmAffinity exports as your user data? Or get some data about movies? Continue reading.

## Usage

### Services
#### Readers
```
from libfa.services.readers.html.exportdata import reader as fahtmlreader

db = fahtmlreader.get_all(basePath)
```

#### Importers
```
from libfa.services.importers.zipdata import main as fazip

db = fazip.exec(zipFilepath)
```

#### Exporters
```
from libfa.services.exporters.csv import main as facsvexporter

facsvexporter.exec(db, filepath.csv)
```

## Contributions
Do you have an improvement or find a bug? Create an issue, you are welcome!


