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


from sys import exit
import logging
from os.path import join, basename, isdir, splitext, expanduser
from shutil import copytree

from .cli import parse_args
from .contexts import CONTEXTS
from .renderer import render_file
from .utils import (
    setup_basic_logging, list_dir_rec, split_ext, make_exec,
    starts_with_shebang)


def main(args):
    """Start hacking the world."""
    status = 0
    templates = join(expanduser('~'), '.tmgr')
    if args.file:
        template_path = join(templates, 'filenames')
        logging.info('using filename templates.')
        for i in args.names:
            base, ext = split_ext(i, base=True)
            CONTEXTS.update({'filename': base})
            template = join(template_path, base + ext)
            logging.info('using %s', template)
            if render_file(template, i, CONTEXTS):
                logging.info('rendered %s', i)
            else:
                logging.info('failed %s', i)
                status = 1
    elif args.directory:
        logging.info('using directory templates.')
        template_path = join(templates, 'directories')
        for i in args.names:
            name = join(
                template_path, basename(i), args.type)
            if isdir(name):
                try:
                    copytree(name, i)
                except (FileExistsError, PermissionError):
                    logging.error('copying files error')
                    logging.warning('ignored %s', i)
                    continue
                for i in list(list_dir_rec(i)):
                    if render_file(i, i, CONTEXTS):
                        logging.info('rendered %s', i)
                    else:
                        logging.info('failed %s', i)
                        status = 1
    else:
        template_path = join(templates, 'extensions')
        logging.info('using extension templates.')
        for i in args.names:
            filename, ext = splitext(basename(i))
            CONTEXTS.update({'filename': filename})
            if not ext or not ext[1:]:
                logging.warning('ignored %s', i)
                continue
            ext = ext[1:]
            template = join(
                template_path, ext, args.type
            ) + '.' + ext
            logging.info('using %s', template)
            if render_file(template, i, CONTEXTS):
                logging.info('rendered %s', i)
            else:
                logging.warning('failed %s', i)
                status = 1
            if starts_with_shebang(i):
                make_exec(i)
    return status


def start_main():
    """Prepare for starting hacking the world."""
    args = parse_args()
    level = logging.WARNING - (args.verbose-args.quiet)*10
    setup_basic_logging(level)
    exit(main(args))
