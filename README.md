## Introduction
Welcome to the FilmAffinity Python Library. My mission is to rescue from the incompatible protocols and formats the platform has :/.

## Requirements
- Python3

> Install python packages with: `sudo pip install -r requirements.txt` :P

## Description
Do you want to convert the zip with html old files that FilmAffinity exports as your user data? Or get some data about movies? Continue reading.

## Usage

### Services
#### Importers
```
import libfa

db = libfa.importer.exportdata.run(zipFilepath)
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

## Tests
Run all with tox: `tox`

## Generate distro
More info: https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
```
python3 setup.py sdist bdist_wheel
```

## Development
Create Virtual Environment: `python -m venv ~/.virtualenvs/libfa-py`
Activate: `. ~/.virtualenvs/libfa-py/bin/activate`
Deactivate: `deactivate`
Install requirements: `pip install requirements.txt`

## Contributions
Do you have an improvement or find a bug? Create an issue, you are welcome!


