## Introduction
Welcome to the FilmAffinity Python Library. My mission is to rescue from the incompatible protocols and formats the platform has :/.

## Requirements
- Python3
- Python3 package: BeautifulSoup4
- Python3 package: [microdata](https://github.com/edsu/microdata)

> Install python packages with: `sudo pip install {packagename}` :P

## Description
Do you want to convert the zip with html old files that FilmAffinity exports as your user data? Or get some data about movies? Continue reading.

## Usage

### Services
#### Importers
```
import libfa

db = libfa.importer.exportdata.exec(zipFilepath)
```

#### Exporters
```
import libfa

libfa.exporter.csv_v1.all(db, /path/you/want/)
libfa.exporter.csv_v1.ratings(db, /path/you/want/filepath.csv)
libfa.exporter.csv_v1.lists(db, /path/you/want/filepath.csv)
libfa.exporter.csv_v1.friends(db, /path/you/want/filepath.csv)
```

#### Web
```
import libfa

movie = libfa.web.v1.get_movie(1234)
results = libfa.web.v1.search('Stalker')
```

## Contributions
Do you have an improvement or find a bug? Create an issue, you are welcome!


