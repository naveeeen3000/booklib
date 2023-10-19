from setuptools import setup, find_packages


setup(
    name='test',
    version='0.0.1',
    description='My private package from private github repo',
    url='https://github.com/naveeeen3000/booklib.git',
    license='unlicense',
    packages=['test', 'test.subpackage', 'test.testmod', 'testmod'],
    zip_safe=False
)