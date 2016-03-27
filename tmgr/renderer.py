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

from jinja2 import Environment
from jinja2.exceptions import TemplateSyntaxError


def render_file(filename, dest, contexts):
    """Render a template file."""
    try:
        with open(filename) as template_file:
            template = template_file.read()
    except (IOError, OSError):
        logging.debug('error reading %s', filename)
        return False
    env = Environment(comment_start_string='{{#',
                      comment_end_string='#}}')
    try:
        renderer = env.from_string(template)
    except TemplateSyntaxError:
        logging.debug('error creating renderer for %s', filename)
        return False
    rendered = renderer.render(contexts)
    try:
        with open(dest, 'w') as rendered_file:
            rendered_file.write(rendered.strip() + '\n')
    except (IOError, OSError):
        logging.debug('error writing %s', dest)
        return False
    return True
