"""
Copyright 2015-2016 Gu Zhengxiong <rectigu@gmail.com>

This file is part of TMgr.

TMgr is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

TMgr is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with TMgr.  If not, see <http://www.gnu.org/licenses/>.
"""


import logging
from sys import stderr
from os.path import join, basename, splitext
from os import stat, chmod, walk
from itertools import chain
from stat import S_IXUSR, S_IXGRP, S_IXOTH, S_ISREG, S_ISDIR


S_IXUGO = S_IXUSR | S_IXGRP | S_IXOTH


def starts_with_shebang(filename):
    """Determine whether the file starts with a shebang line."""
    try:
        with open(filename) as stream:
            return stream.read(2) == '#!'
    except (IOError, OSError):
        return False


def make_exec(filename):
    """Add executable mode to the file."""
    mode = stat(filename).st_mode
    if not S_ISREG(mode) and not S_ISDIR(mode):
        return False
    chmod(filename, mode | S_IXUGO)
    return mode


def list_dir_rec(path='.', ignored=None, followlinks=False):
    """List files in the directory recursively."""
    if ignored is None:
        ignored = []
    files = []
    for i in walk(path, followlinks=followlinks):
        remove_many(i[1], ignored)
        files = chain(
            files,
            (lambda x: (join(x[0], i) for i in x[2]))(i))
    return files


def remove_many(original, many):
    """Remove a list of items from the original list."""
    for one in many:
        if one in original:
            original.remove(one)


def split_ext(path, base=True):
    """Wrap them to make life easier."""
    if base:
        path = basename(path)
    return splitext(path)


def setup_basic_logging(level):
    """Setup the root logger with a debug-only formatter."""
    handler = logging.StreamHandler(stderr)
    handler.setFormatter(DebugFormatter())
    logging.root.addHandler(handler)
    logging.root.setLevel(level)


class DebugFormatter(logging.Formatter):
    """Formatter for logging.debug only."""
    debug_formatter = logging.Formatter(
        '%(module)s.%(funcName)s: %(message)s'
    )

    def __init__(self):
        logging.Formatter.__init__(self)

    def format(self, record):
        if record.levelno == logging.DEBUG:
            return self.debug_formatter.format(record)
        return record.getMessage()
