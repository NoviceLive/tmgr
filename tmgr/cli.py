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


import argparse


PROGRAM_NAME = 'TMgr'
__version__ = '0.2.1'


def parse_args():
    """Parse the commandline arguments."""
    parser = argparse.ArgumentParser(
        description='Templated Touch',
        epilog='the default is using extension templates.')
    parser.add_argument(
        'names', metavar='NAME', nargs='+',
        help='touch this names.')
    template_type = parser.add_mutually_exclusive_group()
    template_type.add_argument(
        '-f', '--file', action='store_true',
        help='use filename templates.')
    template_type.add_argument(
        '-d', '--directory', action='store_true',
        help='use directory templates.')
    parser.add_argument(
        '-t', '--type', default='default',
        help='use the specified minor template.')
    logging_level = parser.add_mutually_exclusive_group()
    logging_level.add_argument(
        '-v', '--verbose', action='count', default=0,
        help='be verbose, -vv for debugging mode.')
    logging_level.add_argument(
        '-q', '--quiet', action='count', default=0,
        help='be quiet, -qq or -qqq for critical or nothing mode.')
    parser.add_argument(
        '-V', '--version', action='version',
        version='{} {}'.format(PROGRAM_NAME, __version__))
    return parser.parse_args()
