# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-25 Bradley M. Bell
# ----------------------------------------------------------------------------
import os
import setuptools
#
# BEGIN_DEPENDENCIES
dependencies = [
   # Always requires to run xrst
   'sphinx', 'toml', 'sphinx-copybutton',
   # Ony required to test xrst
   'pytest',
   # Only required if used in xrst configure file
   'pyspellchecker', 'pyenchant',
   # Only required if used in xrst configure file
   'furo', 'sphinx-rtd-theme', 'sphinx-book-theme',
]
if os.name == 'nt' :
   # pyenchant is not available on windows conda-forge
   dependencies.remove('pyenchant')
# END_DEPENDENCIES
#
# setuptools.setup
setuptools.setup(
   install_requires = dependencies,
)
