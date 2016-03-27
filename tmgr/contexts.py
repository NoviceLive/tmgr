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


from datetime import date


# TODO: Use an configuration file.
CONSTANTS = {
    'name': 'Gu Zhengxiong',
    'email': 'rectigu@gmail.com'
}


CONTEXTS = {
    'copyright': 'Copyright {} {} <{}>'.format(
        date.today().year, CONSTANTS['name'], CONSTANTS['email']
    )
}


CONTEXTS.update(CONSTANTS)
