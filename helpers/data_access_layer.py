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
import sqlite3

# Class to manage connecting to the database.
class DataAccessLayer(object):
	def __init__(self):
		self._connection = sqlite3.connect('db/tasks.db')

	def execute_statement(self, statement):
		cur = self._connection.cursor()
		cur.execute(statement)

		data = cur.fetchall()
		return data

	def execute_modify_statement(self, statement):
		with self._connection:
			cur = self._connection.cursor()
			cur.execute(statement)
			
	# Private objects.
	_connection = None