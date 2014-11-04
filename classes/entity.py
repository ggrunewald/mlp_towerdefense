
from classes.entity import *

class Entity(object):
	_x = 0
	_y = 0

	def __init__(self, x, y):
		self._x = x
		self._y = y

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, n):
			self._x = n

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, n):
			self._y = n
