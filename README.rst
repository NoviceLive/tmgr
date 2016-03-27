tmgr
====


A template manager for the command line.


Installation
============

``pip install tmgr``.


Preparation
===========

Clone templates using ``scripts/update.sh`` or write your own.


Usage
=====

See ``tmgr --help``.

::

   tmgr --help
   usage: tmgr [-h] [-f | -d] [-t TYPE] [-v | -q] [-V] NAME [NAME ...]

   Templated Touch

   positional arguments:
     NAME                  touch this names.

   optional arguments:
     -h, --help            show this help message and exit
     -f, --file            use filename templates.
     -d, --directory       use directory templates.
     -t TYPE, --type TYPE  use the specified minor template.
     -v, --verbose         be verbose, -vv for debugging mode.
     -q, --quiet           be quiet, -qq or -qqq for critical or nothing mode.
     -V, --version         show program's version number and exit

   the default is using extension templates.


Integration
===========

The following example won't work outside Unish_
and may not be up to date.

See Unish_/src/smart.sh.

::

   unalias_if_exists e

   e() {
       : "
   Smart Emacs.

   Usage: e <name> <options>

   Open an existing file using Emacs or create a new one using tmgr.
   "
       local name="${1}"
       local templator='tmgr'
       if [[ -f "${name}" ]]
       then
           emacs "${name}" &
       elif exists ${templator}; then
           ${templator} "${@}" \
               || warning "The File '${name}' is not Templated"
           emacs "${name}" &
       else
           warning "${templator} Unavailable"
           emacs "${name}" &
       fi
   }


.. _Unish: https://github.com/NoviceLive/unish
