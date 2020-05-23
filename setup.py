import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='libfa-py',
      version='0.1',
      author='Andres Mazzo',
      author_email='admin@andresmazzo.com',
      description='FilmAffinity Python Library',
      long_description=long_description,
      url='https://github.com/andresmazzo/libfa-py',
      # packages=setuptools.find_packages('libfa', exclude=["*_test.py"]),
      license='GPL',
      python_requires='>=3.6',
)