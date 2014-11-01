
from classes.entity import *

class Entity(object):
	_x = 0
	_y = 0


	def __init__(self, x, y):
		self._x = x
		self._y = y

	def get_x(self):
		return self._x

	def set_x(self, x):
		self._x = x

	def get_y(self):
		return self._y

	def set_y(self, y):
		self._y = y
