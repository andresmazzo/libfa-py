from setuptools import setup, find_packages
 
setup(name='libfa-py',
      version='0.1',
      url='https://github.com/andresmazzo/libfa-py',
      license='GPL',
      author='Andres Mazzo',
      author_email='admin@andresmazzo.com',
      description='FilmAffinity Python Library',
      packages=find_packages(exclude=['docs', 'tests']),
      long_description=open('README.md').read(),
      zip_safe=False)