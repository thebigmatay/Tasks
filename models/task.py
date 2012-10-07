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
sys.path.append('models')
sys.path.append('errors/models')

import data_access_layer
import tasks_user
import save_error

# Alias class names for easier readability.
DAL = data_access_layer.DataAccessLayer
User = tasks_user.User
SaveError = save_error.SaveError

# Data structure encapulsating a task.
class Task(object):
	# Initialize the task.
	def __init__(self):
		# Initialize the private variables.
		self._id = None
		self._title = ""
		self._description = ""
		self._completed = False
		self._assigned = None

	def save(self):
		# Determine if the task is completed.
		completed_string = "0"
		if self._completed == True:
			completed_string = "1"

		# Determine if there is an assigned user to save.
		assigned_id = -1
		if not self._assigned:
			assigned_id = -1
		else:
			assigned_id = User.get_id(self._assigned)
			if not assigned_id:
				raise SaveError("Assigned user must be saved before saving task.")

		if not self._id:
			# This has never been saved.
			statement = "INSERT INTO tasks (title, description, completed, assigned_id) "
			values = "VALUES ('{0}', '{1}', '{2}', {3})".format(
				self._title,
				self._description,
				completed_string,
				assigned_id)

			statement = statement + values
			dal = data_access_layer.DataAccessLayer()
			DAL.execute_modify_statement(dal, statement)

			# Retrieve the newly created ID.
			ret_statement = "SELECT id FROM tasks ORDER BY id DESC LIMIT 1"
			rows = data_access_layer.DataAccessLayer.execute_statement(dal, ret_statement)
			self._id = rows[0][0]
		else:
			# This has been saved, just update.
			statement = "UPDATE tasks SET "
			values = "title='{0}', description='{1}', completed={2}, assigned_id={3} ".format(
				self._title,
				self._description,
				completed_string,
				assigned_id)
			where = "WHERE id={0}".format(self._id)
			
			statement = statement + values + where
			dal = data_access_layer.DataAccessLayer()
			DAL.execute_modify_statement(dal, statement)

	def load(self, id):
		statement = "SELECT * FROM tasks WHERE id={0}".format(id)
		dal = DAL()
		rows = DAL.execute_statement(dal, statement)

		# Parse each element if found.
		return_value = True
		if len(rows) > 0:
			self._id = rows[0][0]
			self._title = rows[0][1]
			self._description = rows[0][2]
			completed_string = rows[0][3]

			if completed_string == "1":
				self._completed = True
			else:
				self._completed = False
		else:
			return_value = False

		return return_value

	#
	# The accessor methods.
	#
	def get_title(self):
		return self._title

	def set_title(self, title):
		self._title = title

	def get_description(self):
		return self._description

	def set_description(self, description):
		self._description = description

	def is_completed(self):
		return self._completed

	def mark_complete(self):
		self._completed = True

	def mark_incomplete(self):
		self._completed = False

	def get_assigned_user(self):
		return self._assigned

	def set_assigned_user(self, user):
		self._assigned = user

	# Private methods.
	_id = None
	_title = None
	_description = None
	_completed = None
	_assigned = None