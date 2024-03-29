# Tasks - A lightweight task management platform.
# Copyright (C) 2012  Jeff Mataya
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

# Exception class to raise when a save cannot occur.
class SaveError(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return repr(self.message)
	