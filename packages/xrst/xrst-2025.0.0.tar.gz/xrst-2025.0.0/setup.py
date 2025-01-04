# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# ----------------------------------------------------------------------------
# This is a temporary fix and duplicates information in pyproject.toml.
# It will be removed when seutptools gets the pyproject.toml dependencies right
from setuptools import setup

setup(
   name             = 'xrst',
   version          = '2025.0.0',
   description      = 'Extract RST files from source code and run Sphinx',
   license          = 'GPL-3.0-or-later',
   keywords         = 'sphinx rst documentation source',
   url              = 'https://github.com/bradbell/xrst',
   packages         = ['xrst'],
   long_description = 'readme.md',
   classifiers      = [
      'Topic :: Documentation :: Sphinx',
      'Development Status :: 5 - Production/Stable',
      'License :: OSI Approved',
      'Operating System :: OS Independent',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Natural Language :: English',
   ],
   install_requires = [
      'sphinx', 'toml', 'sphinx-copybutton',           # required
      'pytest',                                        # used for testing xrst
      'pyspellchecker', 'pyenchant',                   # only need ones you use
      'furo', 'sphinx-rtd-theme', 'sphinx-book-theme', # only need ones you use
   ],
   entry_points = {
      'console_scripts' : [ 'xrst = xrst:run_xrst' ]
   }
)
