# LIBFA

Welcome to the **FilmAffinity Python Library**. My mission is to rescue from the incompatible protocols and formats the platform has :/.

**IMPORTANT:** Package is in alpha stage and active development.

![status](https://img.shields.io/static/v1?label=status&message=ALPHA&color=yellow)
![license](https://img.shields.io/github/license/andresmazzo/libfa-py)
![size](https://img.shields.io/github/languages/code-size/andresmazzo/libfa-py)
![coverage](https://img.shields.io/static/v1?label=coverage&message=~80%&color=green)
![stars](https://img.shields.io/github/stars/andresmazzo/libfa-py?style=social)

The only requirement is **python** :P.

## Description
Do you want to convert the zip with html old files that FilmAffinity exports as your user data? Or get some data about movies from the web? Continue reading.

## Setup
Create virtual env, activate and install packages.
```
python3 -m venv ~/.virtualenvs/libfa-py
. ~/.virtualenvs/libfa-py/bin/activate
pip install -r requirements.txt
```

## Usage
Super easy!

Actually there are three services: Web, Importer, Exporter.
See [docs](/docs) for more info.

Run `python3` to fire up a python command line. Then just play..
```
import libfa

movie = libfa.web.v1.movie('ar', '534365')
db = libfa.importer.exportdata.run('/path/you/have/filepath.zip')
libfa.exporter.csv_v1.ratings(db, '/path/you/want/filepath.csv')
```


## Development

**Virtual environment:**
- Create: `python3 -m venv ~/.virtualenvs/libfa-py`
- Activate: `. ~/.virtualenvs/libfa-py/bin/activate`
- Exit: `deactivate`

**Install requirements:** 
`pip install requirements.txt`

**Tests:**
- All: `tox` 
- Unit: `pytest libfa --cov=libfa`
>If you modify requirements.txt, then run tox with: `tox --recreate`

**Generate distro:**
`python3 setup.py sdist bdist_wheel`

More info in https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives

## Contributions
Do you have an improvement or find a bug? Create an issue, you are welcome!


