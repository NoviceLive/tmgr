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
