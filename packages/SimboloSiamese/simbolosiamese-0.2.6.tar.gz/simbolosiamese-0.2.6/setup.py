from setuptools import setup, find_packages

with open('README.md','r', encoding='utf-8') as f:
  description = f.read()

setup(
    name='SimboloSiamese', # this is the package folder that contain the "main.py"
    version='0.2.6', # to increment this version number for each new version of this package
    packages=find_packages(), 
    install_requires=[ # dependencies for this package
    # e.g. 'numpy>=1.11.1'
    ],
    entry_point={"console_scripts": [
      "Siamese = Siamese:*",
    ],},
    long_description=description,
    long_description_content_type= "text/markdown",
    contributor="Zawgyi to Unicode and Unicode to Zawgyi: Ye Bhone Lin",
    author="Syallable: Phyo Thu Htet, Zawgyi to Unicode and Unicode to Zawgyi: Min Thiha Htun,  Romanized: Ye Bhone Lin, Supervisor: Phyo Thu Htet",
)