#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# -----------------------------------------------------------------------------
if [ $# != 2 ]
then
   echo 'usage: bin/devel_tools.sh dest_repo spdx_license_id'
   echo 'Copies the current development tools from xrst.git to dest_repo/bin'
   echo 'spdx_license_id is the SPDX-License-Identifier for files in direcory'
   exit 1
fi
dest_repo="$1"
spdx_license_id="$2"
if [ ! -d "$dest_repo/.git" ]
then
   echo "dev_tools.sh: $dest_repo is not a git repository"
   exit 1
fi
if [ ! -d "$dest_repo/bin" ]
then
   echo "dev_tools.sh: $dest_repo/bin is not a diretory"
   exit 1
fi
#
# sed
source bin/grep_and_sed.sh
# -----------------------------------------------------------------------------
# dev_tools
dev_tools='
   check_copy.sh
   check_invisible.sh
   check_sort.sh
   check_tab.sh
   check_version.sh
   dev_settings.sh
   git_commit.sh
   grep_and_sed.sh
   sort.sh
'
for file in $dev_tools
do
   if [ $file == dev_settings.sh ] || [ $file == grep_and_sed.sh ]
   then
      if [ -x bin/$file ]
      then
         echo "bin/$file is executable"
         exit 1
      fi
   else
      line_two=$($sed -n -e '2,2p' bin/$file)
      if [ "$line_two" != 'set -e -u' ]
      then
         echo "Line 2 of bin/$file is not equal to:"
         echo 'set -e -u'
         exit 1
      fi
   fi
done
#
# xrst_repo
xrst_repo=$(pwd)
#
# dest_repo
cd $dest_repo
#
# sed.$$
cat << EOF > sed.$$
s|\\(SPDX-License-Identifier:\\) GPL-3.0-or-later|\\1 $spdx_license_id|
s|^spdx_license_id=.*|spdx_license_id='$spdx_license_id'|
EOF
#
# check for overwriting changes
for file in $dev_tools
do
   dest_path="$dest_repo/bin/$file"
   xrst_path="$xrst_repo/bin/$file"
   $sed -f sed.$$ $xrst_path > temp.$$
   if [ -e $dest_path ]
   then
      if ! diff $dest_path temp.$$ > /dev/null
      then
         temp=$(git ls-files bin/$file)
         if [ "$temp" == '' ]
         then
            echo "$dest_path"
            echo 'not in repository and has changes that would be overwritten'
            rm temp.$$
            rm sed.$$
            exit 1
         else
            if ! git diff --exit-code bin/$file > /dev/null
            then
               echo "$dest_path"
               echo 'is in repository and has changes that are not checked in'
               rm temp.$$
               rm sed.$$
               exit 1
            fi
         fi
      fi
   fi
done
rm temp.$$
#
echo "Copying the following files into $dest_repo/bin"
echo "and setting SPDX-License-Identifier to $spdx_license_id"
for file in $dev_tools
do
   echo "bin/$file"
   dest_path="$dest_repo/bin/$file"
   xrst_path="$xrst_repo/bin/$file"
   $sed -f sed.$$ $xrst_path > $dest_path
   if [ -x "$xrst_path" ]
   then
      chmod +x $dest_path
   fi
done
rm sed.$$ 
# -----------------------------------------------------------------------------
echo
cat << EOF
You probably need to edit the settings in
   $dest_repo/bin/dev_settings.sh
The following, in $dest_repo, will revert to its previous version:
   git show HEAD:bin/dev_settings.sh > bin/dev_settings.sh

Also look for SECTION THAT DEPENDS ON GIT REPOSITORY" in
   $dest_repo/bin/check_version.sh
The following, in $dest_repo, will revert to its previous version:
   git show HEAD:bin/check_version.sh > bin/check_version.sh

dev_tools.sh: OK
EOF
exit 0
