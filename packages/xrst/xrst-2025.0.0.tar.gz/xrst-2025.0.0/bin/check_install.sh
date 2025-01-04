#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_install.sh" ]
then
   echo "bin/check_install.sh: must be executed from its parent directory"
   exit 1
fi
# -----------------------------------------------------------------------------
#
# prefix
prefix="$(pwd)/build/prefix"
#
# test_driver
test_driver='pytest/test_rst.py'
if ! grep '^test_installed_version = False$' $test_driver > /dev/null
then
   echo "bin/check_install.sh: cannot find following in $test_driver"
   echo 'test_installed_verison = False'
   exit 1
fi
#
# install
pip install --prefix=$prefix .
#
# PYTHONPATH
site_packages="$(find $prefix -name 'site-packages' | head -1)"
if [ "$site_packages" == '' ]
then
   echo "bin/check_install.sh: cannot find site-packages below $prefix"
   exit 1
fi
if [ -z "${PYTHONPATH+x}" ]
then
   PYTHONPATH="$site_packages"
elif [ "$PYTHONPATH" == '' ]
then
   PYTHONPATH="$site_packages"
else
   PYTHONPATH="$site_packages:$PYTHONPATH"
fi
export PYTHONPATH
#
# PATH
PATH="$prefix/bin:$PATH"
#
# test_driver
sed -i -e 's|test_installed_version = False|test_installed_version = True|' \
   $test_driver
#
# pytest
pytest -s pytest
#
# test_driver
sed -i -e 's|test_installed_version = True|test_installed_version = False|' \
   $test_driver
#
# -----------------------------------------------------------------------------
echo 'check_install.sh: OK'
exit 0
