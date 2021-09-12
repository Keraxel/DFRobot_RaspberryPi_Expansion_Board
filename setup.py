import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "RaspberryPi_Expansion_Board",
    version = "1.0.0",
    author = "DFRobot",
    description = ("DFRobot RaspberryPi Expansion Board"),
    license = "MIT",
    keywords = "DFRobot,RaspberryPi",
    url = "https://github.com/Keraxel/DFRobot_RaspberryPi_Expansion_Board",
    packages=['RaspberryPi_Expansion_Board'],
    long_description=read('readme.md'),
    install_requires=[
        "smbus"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "License :: OSI Approved :: MIT License",
    ],
)