#! /usr/bin/env bash
set -e -u
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-24 Bradley M. Bell
# ----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
   echo $*
   eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != 'bin/run_xrst.sh' ]
then
   echo 'must execut bin/run_xrst.sh from its parent directory'
   exit 1
fi
# -----------------------------------------------------------------------------
if [ "$#" != 1 ] && [ "$#" != 2 ]
then
   echo \
   'bin/run_xrst.sh (html|tex) [(--rst_line_numbers|--replace_spell_commands)]'
   exit 1
fi
if [ "$1" != 'html' ] && [ "$1" != 'tex' ]
then
   echo 'bin/run_xrst.sh first argument not html or tex'
   exit 1
fi
target="$1"
extra_flag=''
if [ "$#" == 2 ]
then
   if [ "$2" != '--rst_line_numbers' ] && [ "$2" != '--replace_spell_commands' ]
   then
      echo 'bin/run_xrst.sh second argument not'
      echo '--rst_line_numbers or --replace_spell_commands'
      exit 1
   fi
   extra_flag="$2"
fi
# -----------------------------------------------------------------------------
# index_page_name
index_page_name=$(\
   sed -n -e '/^ *--index_page_name*/p' .readthedocs.yaml | \
   sed -e 's|^ *--index_page_name *||' \
)
# -----------------------------------------------------------------------------
echo_eval python -m xrst  \
   --page_source \
   --group_list      default user dev \
   --html_theme      furo \
   --target          $target \
   --index_page_name $index_page_name \
   $extra_flag
# -----------------------------------------------------------------------------
echo 'run_xrst.sh: OK'
exit 0
