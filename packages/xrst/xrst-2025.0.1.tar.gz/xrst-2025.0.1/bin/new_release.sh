#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# -----------------------------------------------------------------------------
year='2025' # Year for this stable version
release='0' # first release for each year starts with 0
# -----------------------------------------------------------------------------
if [ $# != 0 ]
then
   echo 'bin/new_release.sh does not expect any arguments'
   exit 1
fi
if [ "$0" != 'bin/new_release.sh' ]
then
   echo 'bin/new_release.sh: must be executed from its parent directory'
   exit 1
fi
if [ ! -e './.git' ]
then
   echo 'bin/new_release.sh: cannot find ./.git'
   exit 1
fi
#
# branch
branch=$(git branch --show-current)
if [ "$branch" != 'master' ]
then
   echo 'bin/new_release.sh: must start execution using master branch'
   exit 1
fi
#
# tag
tag=$year.0.$release
if git tag --list | grep "$tag" > /dev/null
then
   if grep "$tag" user/user.xsrt
   then
      echo "The tag $tag already exists"
      echo 'and user/user.xrst has been modified to use it.'
      exit 1
   fi
fi
#
# stable_branch
stable_branch=stable/$year
#
# stable_local_hash
pattern=$(echo " *refs/heads/$stable_branch" | sed -e 's|/|[/]|g')
stable_local_hash=$(
   git show-ref $stable_branch | \
      sed -n -e "/$pattern/p" | \
         sed -e "s|$pattern||"
)
#
# stable_remote_hash
pattern=$(echo " *refs/remotes/origin/$stable_branch" | sed -e 's|/|[/]|g')
stable_remote_hash=$(
   git show-ref $stable_branch | \
      sed -n -e "/$pattern/p" | \
         sed -e "s|$pattern||"
)
#
# master_local_hash
pattern=$(echo " *refs/heads/master" | sed -e 's|/|[/]|g')
master_local_hash=$(
   git show-ref master | \
      sed -n -e "/$pattern/p" | \
         sed -e "s|$pattern||"
)
#
# master_remote_hash
pattern=$(echo " *refs/remotes/origin/master" | sed -e 's|/|[/]|g')
master_remote_hash=$(
   git show-ref master | \
      sed -n -e "/$pattern/p" | \
         sed -e "s|$pattern||"
)
#
# ----------------------------------------------------------------------------
# Changes to master branch
# ----------------------------------------------------------------------------
#
# user.xrst
if git tag --list | grep "$tag" > /dev/null
then
   # Delay doing this update until the remove tag exists.
   sed -i user/user.xrst \
      -e "s|stable-[0-9]\{4\}|stable-$year|g" \
      -e "s|release-[0-9]\{4\}|release-$year|g" \
      -e "s|archive/[0-9]\{4\}[.]0[.][0-9]*.tar.gz|archive/$tag.tar.gz|"
fi
#
# check_version
# use current date for version on master branch
if ! bin/check_version.sh
then
   echo 'Continuing even thought bin/check_version made changes.'
fi
#
# git_status
git_status=$(git status --porcelain)
if [ "$git_status" != '' ]
then
   echo 'bin/new_release: git staus --porcelean is not empty for master branch'
   echo 'use bin/git_commit.sh to commit its changes ?'
   exit 1
fi
# ----------------------------------------------------------------------------
# Changes to stable branch
# ----------------------------------------------------------------------------
if ! git show-ref $stable_branch > /dev/null
then
   echo "bin/new_release: neither local or remvoe $stable_branch exists."
   echo 'Use the following to create it ?'
   echo "   git branch $stable_branch"
   exit 1
fi
if ! git checkout $stable_branch
then
   echo "bin/new_release: should be able to checkout $stable_branch"
   exit 1
fi
#
# user.xrst
if git tag --list | grep "$tag" > /dev/null
then
   # Delay doing this update until the remove tag exists.
   sed -i user/user.xrst \
      -e "s|stable-[0-9]\{4\}|stable-$year|g" \
      -e "s|release-[0-9]\{4\}|release-$year|g" \
      -e "s|archive/[0-9]\{4\}[.]0[.][0-9]*.tar.gz|archive/$tag.tar.gz|"
fi
#
# pyproject.toml
sed -i pyproject.toml \
-e "s|version\\( *\\)= *'[0-9]\\{4\\}[.][0-9]*[.][0-9]*'|version\\1= '$tag'|"
version=$(
   sed -n -e '/^ *version *=/p' pyproject.toml | \
      sed -e 's|^ *version *= *||' -e "s|'||g"
)
if [ "$version" != "$tag" ]
then
   echo "bin/rew_release: branch = $stable_branch"
   echo "Version number should be $tag in pyproject.toml"
   exit 1
fi
if ! bin/check_version.sh
then
   echo 'Continuing even thought bin/check_version made changes.'
fi
#
# check_xrst.sh
bin/check_xrst.sh
#
# check_all
bin/check_all.sh
#
# git_status
git_status=$(git status --porcelain)
if [ "$git_status" != '' ]
then
   echo "bin/new_release: git staus --porcelean not empty for $stable_branch"
   echo 'use bin/git_commit.sh to commit its changes ?'
   exit 1
fi
# -----------------------------------------------------------------------------
#
# stable_remove
if [ "$stable_remote_hash" == '' ]
then
   empty_hash='yes'
   echo "bin/new_release: remote $stable_branch does not exist."
   echo 'Use the following to create it ?'
   echo "   git push origin $stable_branch"
   exit 1
fi
if [ "$stable_local_hash" != "$stable_remote_hash" ]
then
   empty_hash='yes'
   echo "bin/new_release: locan and remote $stable_branch differ."
   echo "local  $stable_local_hash"
   echo "remote $stable_remote_hash"
   echo 'Use git push to fix this ?'
   exit 1
fi
#
# push tag
if ! git tag --list | grep "$tag" > /dev/null
then
   read -p 'commit release or abort [c/a] ?' response
   if [ "$response" == 'a' ]
   then
      exit 1
   fi
   echo "git tag -a -m 'created by new_release.sh' $tag $stable_remote_hash"
   git tag -a -m 'created by new_release.sh' $tag $stable_remote_hash
   #
   echo "git push origin $tag"
   git push origin $tag
fi
#
# user.xrst
if ! grep "$tag.tar.gz" user/user.xrst > /dev/null
then
   echo 'bin/new_release.sh: must re-run to update user.xrst'
   exit 1
fi
# ----------------------------------------------------------------------------
git checkout master
#
# user.xrst
if ! grep "$tag.tar.gz" user/user.xrst > /dev/null
then
   echo "bin/new_release.sh: execpted user.xrst to use $tag.tar.gz"
   exit 1
fi
#
# master_remote
if [ "$master_local_hash" != "$master_remote_hash" ]
then
   echo 'bin/new_release.sh: local and remote master differ'
   echo "local  $mster_local_hash"
   echo "remote $master_remode_hash"
   echo 'Use git push to fix this ?'
   exit 1
fi
#
#
echo 'bin/new_release.sh: OK'
exit 0
