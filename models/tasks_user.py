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
sys.path.append('helpers')
import data_access_layer

# Alias class names for easier readability.
DAL = data_access_layer.DataAccessLayer

# Data structure encapulsating a task.
class User(object):
	# Initialize the task.
	def __init__(self):
		# Initialize the private variables.
		self._id = None
		self._name = ""
		self._email = ""

	def save(self):
		if not self._id:
			# This has never been saved.
			statement = "INSERT INTO users (name, email) "
			values = "VALUES ('{0}', '{1}')".format(self._name, self._email)

			statement = statement + values
			dal = data_access_layer.DataAccessLayer()
			DAL.execute_modify_statement(dal, statement)

			# Retrieve the newly created ID.
			ret_statement = "SELECT id FROM users ORDER BY id DESC LIMIT 1"
			rows = data_access_layer.DataAccessLayer.execute_statement(dal, ret_statement)
			self._id = rows[0][0]
		else:
			# This has been saved, just update.
			statement = "UPDATE users SET "
			values = "name='{0}', email='{1}' ".format(
				self._name,
				self._email)
			where = "WHERE id={0}".format(self._id)
			
			statement = statement + values + where
			dal = data_access_layer.DataAccessLayer()
			DAL.execute_modify_statement(dal, statement)

	def load(self, id):
		statement = "SELECT * FROM users WHERE id={0}".format(id)
		dal = DAL()
		rows = DAL.execute_statement(dal, statement)

		# Parse each element if found.
		return_value = True
		if len(rows) > 0:
			self._id = rows[0][0]
			self._name = rows[0][1]
			self._email = rows[0][2]
		else:
			return_value = False

		return return_value

	#
	# The accessor methods.
	#
	def get_id(self):
		return self._id

	def get_name(self):
		return self._name

	def set_name(self, name):
		self._name = name

	def get_email(self):
		return self._email

	def set_email(self, email):
		self._email = email

	# Private methods.
	_id = None
	_name = None
	_email = None