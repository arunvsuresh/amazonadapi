from distutils.core import setup

setup(
    name='amazonadapi',
    version='0.0.4',
    author='Jim Barcelona, Arun Suresh',
    author_email='barce@me.com, arunvsuresh@gmail.com',
    packages=['amazonadapi', 'amazonadapi.tests'],
    install_requires=[
      'future',
    ],
    scripts=[],
    url='https://github.com/barce/amazonadapi',
    license='LICENSE',
    description='A client for interacting with the Amazon Ad API.',
    long_description=open('README.txt').read(),
)
 
