#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['pipeless_plant_bringup'],
    package_dir={'': 'scripts'},
    )

setup(**d)
