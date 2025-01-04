#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# -----------------------------------------------------------------------------
# echo_eval
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/check_all.sh" ]
then
   echo "bin/check_all.sh: must be executed from its parent directory"
   exit 1
fi
#
# sed
source bin/grep_and_sed.sh
#
# internet
internet='yes'
if [ "$#" != 0 ]
then
   if [ "$1" != 'no_internet' ] || [ "$#" != 1 ]
   then
      echo 'usage: bin/check_all.sh [no_internet]'
      exit 1
   fi
   internet='no'
fi
#
# check_list, bin/check_xrst.sh
if [ "$internet" == 'yes' ]
then
   check_list=$(ls bin/check_*)
else
   check_list=$(ls bin/check_* | $sed -e '/^bin[/]check_install.sh/d' )
   $sed -e 's|# TEMPORARY COMMENT:||g' -i bin/check_xrst.sh
   $sed -e '/--external_links/s|^|# TEMPORARY COMMENT:|' -i bin/check_xrst.sh
fi
for check in $check_list
do
   if [ "$check" != 'bin/check_all.sh' ]
   then
      echo_eval $check
   fi
done
#
# bin/check_xrst.sh
if [ "$internet" == 'no' ]
then
   $sed -e 's|^# TEMPORARY COMMENT:||' -i bin/check_xrst.sh
fi
#
# tox
tox
#
if [ "$internet" == 'no' ]
then
   echo 'check_all.sh no_internet: OK'
else
   echo 'check_all.sh: OK'
fi
exit 0
